from apps.recommendation.services import RecommendationService

from apps.recommendation.exports.excel_export import ExcelExport
from apps.recommendation.exports.pdf_export import PDFExport


def export_excel(request):

    ranking = RecommendationService.generate()

    return ExcelExport.export(ranking)


def export_pdf(request):

    ranking = RecommendationService.generate()

    return PDFExport.export(ranking)