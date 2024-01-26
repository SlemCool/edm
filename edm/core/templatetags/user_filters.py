from django import template
from documents.models import Theme

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def add_placeholder(field, placeholder=None):
    field.field.widget.attrs["placeholder"] = (
        placeholder if placeholder is not None else field.field.help_text
    )
    return field


@register.simple_tag()
def tag_themes():
    return Theme.objects.all()
