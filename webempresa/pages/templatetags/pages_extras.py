#hacer su propio tag

from django import template
from pages.models import Page

register=template.Library()

#{% load pages_extras    %}

#se registe el tag
@register.simple_tag
def get_page_list():
    pages=Page.objects.all()
    return pages