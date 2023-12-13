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

admin.site.register(Document)
admin.site.register(Organization)
admin.site.register(Numeration)
admin.site.register(Theme)
admin.site.register(Detail)
admin.site.register(Given)
admin.site.register(Implementers)
