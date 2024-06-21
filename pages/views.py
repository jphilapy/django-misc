from typing import Any
from django.views.generic import TemplateView
from .models import Project


class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):  # new
    template_name = "about.html"


class TestVarPageView(TemplateView):
    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Hello World"
        return context

class ListPageView(TemplateView):
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list = Project.objects.all()
        context['list_items'] = list
        return context

class DetailPageView(TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        list_id = kwargs["id"] # get user id
        selected_list = Project.objects.get(pk=list_id);
        
        context['list_item'] = selected_list
        return context
