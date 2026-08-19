"""
Tool-tool yang boleh dipanggil chatbot publik.

ATURAN KETAT:
- Semua fungsi di sini HANYA membaca data AGREGAT per desa
  (cluster, skor rekomendasi, indikator dominan).
- TIDAK ADA fungsi yang mengakses data pribadi responden
  (nama, NIK, jawaban individu). Kalau perlu data baru,
  tambahkan lewat service yang sudah ada, JANGAN query
  langsung ke model Respondent/Response di sini.
"""

from apps.analytics.services.feature_importance_service import (
    FeatureImportanceService,
)
from apps.analytics.services.ml_dashboard_service import (
    MLDashboardService,
)
from apps.master.models import Village
from apps.recommendation.services.recommendation_service import (
    RecommendationService,
)


def list_villages(**kwargs):

    names = list(
        Village.objects.values_list("name", flat=True).order_by("name")
    )

    return {
        "total": len(names),
        "villages": names,
    }


def get_village_info(village_name, **kwargs):

    village = (
        Village.objects
        .filter(name__iexact=village_name.strip())
        .select_related("cluster")
        .first()
    )

    if village is None:

        return {
            "found": False,
            "message": (
                f"Desa \"{village_name}\" tidak ditemukan di sistem."
            ),
        }

    ranking = RecommendationService.dashboard().get("ranking", [])

    # FIXED: ranking sekarang berupa list of dict hasil cache
    # (village_id, village_name, ...) -- BUKAN objek Django lagi.
    match = next(
        (
            item
            for item in ranking
            if item["village_id"] == village.id
        ),
        None,
    )

    return {

        "found": True,

        "village": village.name,

        "cluster": (
            village.cluster.name if village.cluster else "Belum dianalisis"
        ),

        "status": match["status"] if match else "Belum ada data",

        "recommendation": (
            match["recommendation"] if match else None
        ),

        "rank": (
            ranking.index(match) + 1 if match else None
        ),

        "total_village_ranked": len(ranking),

    }


def get_top_villages(limit=5, **kwargs):

    ranking = RecommendationService.dashboard().get("ranking", [])

    limit = max(1, min(int(limit or 5), 24))

    top = ranking[:limit]

    return {

        "villages": [

            {

                "rank": index + 1,

                # FIXED: village_name langsung (dict), bukan
                # item["village"].name (objek).
                "village": item["village_name"],

                "status": item["status"],

                "recommendation": item["recommendation"],

            }

            for index, item in enumerate(top)

        ],

    }


def get_dominant_factors(**kwargs):

    variables = FeatureImportanceService.dominant_variables()

    return {

        "factors": [

            {

                "name": item["name"],

                "percentage": item["percentage"],

            }

            for item in variables[:5]

        ],

    }


def get_general_summary(**kwargs):

    variable_importance = FeatureImportanceService.dominant_variables()

    summary = MLDashboardService.summary()

    narrative = MLDashboardService.narrative_summary(
        variable_importance,
    )

    return {

        "total_village": summary["total_village"],

        "n_clusters": summary["n_clusters"],

        "narrative": narrative,

    }


TOOL_REGISTRY = {

    "list_villages": list_villages,

    "get_village_info": get_village_info,

    "get_top_villages": get_top_villages,

    "get_dominant_factors": get_dominant_factors,

    "get_general_summary": get_general_summary,

}


TOOLS_SCHEMA = [

    {
        "name": "list_villages",
        "description": (
            "Ambil daftar semua nama desa wisata yang ada di sistem."
        ),
        "input_schema": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "name": "get_village_info",
        "description": (
            "Ambil status dan rekomendasi untuk SATU desa wisata "
            "tertentu berdasarkan namanya."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "village_name": {
                    "type": "string",
                    "description": (
                        "Nama desa, contoh: 'Punten' atau 'Tlekung'."
                    ),
                },
            },
            "required": ["village_name"],
        },
    },

    {
        "name": "get_top_villages",
        "description": (
            "Ambil daftar desa wisata dengan peringkat/prioritas "
            "rekomendasi tertinggi."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": (
                        "Jumlah desa yang ingin ditampilkan "
                        "(default 5, maksimal 24)."
                    ),
                },
            },
        },
    },

    {
        "name": "get_dominant_factors",
        "description": (
            "Ambil faktor/indikator yang paling berpengaruh terhadap "
            "karakteristik desa wisata secara umum."
        ),
        "input_schema": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "name": "get_general_summary",
        "description": (
            "Ambil ringkasan umum kondisi seluruh desa wisata "
            "Kota Batu (jumlah desa, jumlah kelompok, kesimpulan)."
        ),
        "input_schema": {
            "type": "object",
            "properties": {},
        },
    },

]


def to_openai_tools_schema():
    """
    DeepSeek pakai format tool-calling ala OpenAI (beda struktur
    dari Anthropic), jadi TOOLS_SCHEMA di atas perlu dikonversi.
    """

    return [

        {
            "type": "function",
            "function": {
                "name": tool["name"],
                "description": tool["description"],
                "parameters": tool["input_schema"],
            },
        }

        for tool in TOOLS_SCHEMA

    ]


def execute_tool(name, tool_input):

    handler = TOOL_REGISTRY.get(name)

    if handler is None:

        return {"error": f"Tool \"{name}\" tidak dikenali."}

    try:

        return handler(**(tool_input or {}))

    except Exception as error:

        return {"error": str(error)}