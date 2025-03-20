from django.urls import path
from apps.news import views

app_name = 'news'

urlpatterns = [
    path("", views.NewsListView.as_view(), name="list"),
    path("<int:pk>/", views.NewsDetailView.as_view(), name="detail"),
    path("create/", views.NewsCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", views.NewsUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.NewsDeleteView.as_view(), name="delete"),
]