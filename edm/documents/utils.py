from django.conf import settings
from django.core.paginator import Paginator


def paginator(objects, request):
    document = Paginator(objects, settings.HOW_MANY_DOCUMENTS)
    page_number = request.GET.get("page")
    return document.get_page(page_number)
