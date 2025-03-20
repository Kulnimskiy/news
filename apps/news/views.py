from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.news.models import News
from django.urls import reverse_lazy


class NewsListView(ListView):
    model = News
    template_name = "news/list.html"
    context_object_name = "news"
    ordering = ["-published_at"]


class NewsDetailView(DetailView):
    model = News
    template_name = "news/detail.html"


class NewsCreateView(CreateView):
    model = News
    template_name = "news/form.html"
    fields = ["title", "body"]


class NewsUpdateView(UpdateView):
    model = News
    template_name = "news/form.html"
    fields = ["title", "body"]


class NewsDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy("news:list")
