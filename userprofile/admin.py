from django.contrib import admin

from .models import UserProfile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id","pkid","user","gender","place"]
    list_filter = ["gender"]
    list_display_links = ["id","pkid","user"]


admin.site.register(UserProfile,ProfileAdmin)
