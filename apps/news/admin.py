from django.contrib import admin
from apps.news.models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "updated_at")
    list_filter = ("published_at",)
    search_fields = ("title", "body")
    ordering = ("-published_at",)
    readonly_fields = ("published_at", "updated_at")

News._meta.get_field("published_at").auto_now_add = True
News._meta.get_field("updated_at").auto_now = True