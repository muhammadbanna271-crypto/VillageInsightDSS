from apps.analytics.models import MLModelRegistry
from apps.master.models import Variable


class FeatureImportanceService:
    """
    Mengambil hasil feature importance (Random Forest) dari
    MLModelRegistry yang aktif, dan menyiapkannya untuk
    ditampilkan di dashboard (chart & radar).
    """

    @staticmethod
    def latest_registry():

        return (
            MLModelRegistry.objects
            .filter(is_active=True)
            .first()
        )

    @classmethod
    def dominant_indicators(cls, top_n=10):

        registry = cls.latest_registry()

        if registry is None:
            return []

        return registry.feature_importance[:top_n]

    @classmethod
    def dominant_variables(cls):
        """
        Feature importance yang sudah diagregasi per variabel,
        dilengkapi nama variabel (bukan cuma code), cocok buat
        Feature Importance Chart & narasi kesimpulan otomatis.
        """

        registry = cls.latest_registry()

        if registry is None:
            return []

        variable_names = {
            variable.code: variable.name
            for variable in Variable.objects.all()
        }

        result = []

        for item in registry.variable_importance:

            result.append({

                "code": item["group"],

                "name": variable_names.get(
                    item["group"],
                    item["group"],
                ),

                "percentage": item["percentage"],

            })

        return result

    @classmethod
    def radar_axes_for_village(cls, village):
        """
        Nilai radar chart per desa: rata-rata skor tiap variabel
        (X1..X5, Y1..Y6) -- 11 axis, sesuai VariableScore yang
        sudah ada.
        """

        scores = (
            village.variable_scores
            .select_related("variable")
            .order_by("variable__code")
        )

        return [

            {

                "code": score.variable.code,

                "name": score.variable.name,

                "score": float(score.score),

            }

            for score in scores

        ]
