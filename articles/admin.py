from django.contrib import admin
from .models import Articles
# Register your models here.

# admin.site.register(Articles)
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "created_at")
    search_fields = ("id", "topic")
    ordering = ("-created_at",)
