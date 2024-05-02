from django.contrib import admin
# Register your models here.
from app.form_model.models.userprofile import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_image']