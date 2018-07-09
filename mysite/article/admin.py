from django.contrib import admin
from article.models import Article
from article.models import Tag
from article.models import Category
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','content','data']
    list_filter = ['title']
    ordering = ['title','content']
    search_fields = ('title',)


admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Category)