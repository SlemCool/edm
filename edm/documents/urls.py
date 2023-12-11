from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", views.index, name="index"),
    path("documents/", views.documents_list, name="documents"),
    path("documents/<int:pk>/", views.document_detail, name="doc_detail"),
    path("documents/<yyyy:year>/", views.documents_archive, name="docs_archive"),
    # FOR EXAMPLE ONLY re_path
    re_path(
        "^documents/(?P<year>[0-9]{4})/$", views.documents_archive, name="docs_archive"
    ),
]
