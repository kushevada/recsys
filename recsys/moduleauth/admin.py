from django.contrib import admin
from .models import Profile


# Register your models here.
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'age', 'height', 'weight', 'goal', 'calorie_adjustment')



admin.site.register(Profile, ProfilesAdmin)