from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def documents_list(request):
    pass


def document_detail(request):
    pass


def documents_archive(request):
    pass