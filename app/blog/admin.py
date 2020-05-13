from django.contrib import admin

from .models import ArticleList


class ArticleListAdmin(admin.ModelAdmin):
    list_display = ("name_article", "art_date", "text_article")
    list_display_links = ("name_article", "art_date", "text_article")
    search_fields = ("name_article", "art_date", "text_article")
    list_per_page = 25


admin.site.register(ArticleList, ArticleListAdmin)
