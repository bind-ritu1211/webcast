from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "pages/webcast/index.html"
class AboutView(TemplateView):
    template_name = "pages/webcast/course/index.html"