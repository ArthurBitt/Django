from django.contrib import admin

from app.model_pagination.models.item import *
# Register your models here.
class PaginationModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Item, PaginationModelAdmin)