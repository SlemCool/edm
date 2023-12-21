from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, "yyyy")
app_name = 'documents'

urlpatterns = [
    path("", views.index, name="index"),
    path('create/', views.document_create, name='document_create'),
    path("documents/<int:document_id>/", views.document_detail, name="document_detail"),
    path("documents/<int:document_id>/edit/", views.document_edit, name="document_edit"),
    path("documents/incoming/", views.document_incoming, name="incoming"),
    path("documents/outgoing/", views.document_outgoing, name="outgoing"),
    # path("documents/", views.documents_list, name="documents"),
    # path("documents/<yyyy:year>/", views.documents_archive, name="docs_archive"),
    # # FOR EXAMPLE ONLY re_path
    # re_path(
    #     "^documents/(?P<year>[0-9]{4})/$", views.documents_archive, name="docs_archive"
    # ),
]
