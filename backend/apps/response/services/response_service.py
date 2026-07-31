from apps.master.models import Questionnaire


class ResponseService:
    """
    Service untuk mengambil data questionnaire.
    """

    @staticmethod
    def get_questionnaires():

        return (
            Questionnaire.objects
            .select_related(
                "indicator",
                "indicator__variable",
            )
            .filter(
                is_active=True,
            )
            .order_by(
                "indicator__variable__code",
                "indicator__code",
                "question_order",
            )
        )