from django.contrib import admin
from .models import Article,Comment

# Register your models here.
admin.site.register(Comment)
@admin.register(Article)
class articleAdmin(admin.ModelAdmin):
    list_display=["title","author","createdDate"]
    list_display_links=["title","author"]
    search_fields=["title"]
    list_filter=["createdDate"]
    class Meta:
        model = Article()