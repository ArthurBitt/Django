from django.contrib import admin
from app.search_model.models.book_model import *
# Register your models here.
class SearchModelAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Book, SearchModelAdmin)
