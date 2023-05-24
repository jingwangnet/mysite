from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Page


# Create your views here.
class AboutPageView(TemplateView):
    template_name = "page/about.html"


class LabPageView(TemplateView):
    template_name = "page/lab.html"


def pages(requets, url):
    page = get_object_or_404(Page, permalink=url)
    context = {"page": page}
    return render(requets, "page/page.html", context)
