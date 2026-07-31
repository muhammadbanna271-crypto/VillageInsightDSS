from apps.recommendation.selectors.recommendation_selector import (
    RecommendationSelector,
)

from apps.recommendation.services.topsis import (
    TOPSIS,
)


class RecommendationService:

    @staticmethod
    def _classify(score):
        """
        Klasifikasi skor preferensi TOPSIS (0-1) jadi status,
        warna badge, dan rekomendasi singkat.
        """

        if score >= 0.7:

            return {

                "status": "Sangat Layak",

                "badge": "success",

                "recommendation": (
                    "Prioritas utama untuk pengembangan desa wisata."
                ),

            }

        if score >= 0.5:

            return {

                "status": "Layak",

                "badge": "primary",

                "recommendation": (
                    "Layak dikembangkan lebih lanjut dengan "
                    "penguatan pada indikator yang masih rendah."
                ),

            }

        if score >= 0.3:

            return {

                "status": "Cukup Layak",

                "badge": "warning",

                "recommendation": (
                    "Perlu perbaikan pada beberapa indikator "
                    "sebelum diprioritaskan."
                ),

            }

        return {

            "status": "Kurang Layak",

            "badge": "danger",

            "recommendation": (
                "Membutuhkan pembenahan signifikan pada "
                "infrastruktur, fasilitas, dan pelayanan."
            ),

        }

    @classmethod
    def _run_topsis(cls):

        villages, indicators, matrix = (
            RecommendationSelector.decision_matrix()
        )

        if not villages:
            return None

        if not indicators:
            return None

        if matrix is None:
            return None

        if len(matrix) == 0:
            return None

        weights = [
            float(ind.weight)
            for ind in indicators
        ]

        criteria = [
            ind.criterion_type
            for ind in indicators
        ]

        topsis = TOPSIS(
            matrix,
            weights,
            criteria,
        )

        result = topsis.rank()

        ranking = []

        for village, score in zip(
            villages,
            result["preference"],
        ):

            score_value = float(score)

            classification = cls._classify(score_value)

            ranking.append(
                {
                    "village": village,
                    "score": score_value,
                    "status": classification["status"],
                    "badge": classification["badge"],
                    "recommendation": classification["recommendation"],
                }
            )

        ranking.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        return {
            "villages": villages,
            "indicators": indicators,
            "matrix": matrix,
            "ranking": ranking,
            "normalized": result["normalized"],
            "weighted": result["weighted"],
            "positive": result["positive"],
            "negative": result["negative"],
            "distance_positive": result["distance_positive"],
            "distance_negative": result["distance_negative"],
            "preference": result["preference"],
        }

    @classmethod
    def generate(cls):

        data = cls._run_topsis()

        if data is None:
            return []

        return data["ranking"]

    @classmethod
    def dashboard(cls):

        data = cls._run_topsis()

        if data is None:

            return {
                "result": [],
                "ranking": [],
                "villages": [],
                "indicators": [],
                "decision_matrix": [],
                "normalized": [],
                "weighted": [],
                "positive": [],
                "negative": [],
                "distance_positive": [],
                "distance_negative": [],
                "preference": [],
            }

        return {

            "result": data["ranking"],

            "ranking": data["ranking"],

            "villages": data["villages"],

            "indicators": data["indicators"],

            "decision_matrix": data["matrix"],

            "normalized": data["normalized"],

            "weighted": data["weighted"],

            "positive": data["positive"],

            "negative": data["negative"],

            "distance_positive": data["distance_positive"],

            "distance_negative": data["distance_negative"],

            "preference": data["preference"],
        }