from django import template
from page.models import Page

register = template.Library()


@register.inclusion_tag("page/links.html")
def show_links():
    pages = Page.objects.all()
    return {"pages": pages}
