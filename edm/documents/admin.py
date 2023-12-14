from django.contrib import admin

from .models import (
    Detail,
    Document,
    Given,
    Implementers,
    Numeration,
    Organization,
    Theme,
)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "doc_type",
        "from_where",
        "area",
        "who",
        "input_num",
        "output_num",
        "theme",
        "detail",
        "given",
        "description",
        "implementers",
    )
    search_fields = (
        "from_where",
        "area",
        "who",
        "theme",
        "detail",
        "description",
        "implementers",
    )
    list_filter = ("doc_type",)
    empty_value_display = "-пусто-"


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
    search_fields = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Numeration)
class NumerationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "num",
    )
    list_editable = ("num",)
    empty_value_display = "-пусто-"


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Given)
class GivenAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Implementers)
class ImplementersAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"
