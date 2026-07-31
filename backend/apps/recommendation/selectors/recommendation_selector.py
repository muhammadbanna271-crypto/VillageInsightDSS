from django.db.models import Avg

from apps.master.models import (
    Village,
    Indicator,
)

from apps.response.models import Response


class RecommendationSelector:
    """
    Selector untuk mengambil matriks keputusan
    berdasarkan rata-rata skor setiap indikator
    pada masing-masing desa.
    """

    @staticmethod
    def villages():
        """
        Semua desa aktif.
        """
        return (
            Village.objects
            .filter(is_active=True)
            .order_by("name")
        )

    @staticmethod
    def indicators():
        """
        Semua indikator aktif.
        """
        return (
            Indicator.objects
            .filter(is_active=True)
            .select_related("variable")
            .order_by(
                "variable__code",
                "code",
            )
        )

    @classmethod
    def decision_matrix(cls):
        """
        Return:

        villages
        indicators
        matrix

        matrix berbentuk:

        [
            [4.2,3.8,4.6],
            [3.9,4.1,4.8],
        ]
        """

        villages = list(
            cls.villages()
        )

        indicators = list(
            cls.indicators()
        )

        matrix = []

        for village in villages:

            row = []

            for indicator in indicators:

                avg = (
                    Response.objects
                    .filter(
                        respondent__survey_village__village=village,
                        questionnaire__indicator=indicator,
                    )
                    .aggregate(
                        value=Avg("score")
                    )["value"]
                )

                if avg is None:
                    avg = 0

                row.append(
                    float(avg)
                )

            matrix.append(row)

        return (
            villages,
            indicators,
            matrix,
        )