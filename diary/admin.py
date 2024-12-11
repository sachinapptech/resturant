from django.contrib import admin
from .models import Cuisine, CuisinePhoto, VisitorProfile, Visit

class CuisinePhotoInline(admin.TabularInline):
    model = CuisinePhoto
    extra = 1
    fields = ('photo',)
    max_num = 10


class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'views')
    search_fields = ('name',)
    list_filter = ('price',)
    inlines = [CuisinePhotoInline]

class VisitorProfileInline(admin.TabularInline):
    model = VisitorProfile
    extra = 1  # Number of empty forms to display (adjust as needed)
    fields = ('user', 'preferred_cuisine') 

class VisitInline(admin.TabularInline):
    model = Visit
    extra = 1  # Number of empty forms to display
    fields = ('cuisine', 'expense', 'comment', 'rating', 'visit_date')  # Fields you want to display


class VisitorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'place', 'email', 'preferred_cuisine')
    search_fields = ('user__username', 'name', 'email')
    list_filter = ('place',)



class VisitAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'cuisine', 'visit_date', 'expense')
    search_fields = ('visitor__name', 'cuisine__name')
    list_filter = ('visit_date', 'cuisine','visitor')
    date_hierarchy = 'visit_date'

# Correctly register models with their admin configurations
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(CuisinePhoto)  # Assuming you want to manage CuisinePhoto directly as well
admin.site.register(VisitorProfile, VisitorProfileAdmin)
admin.site.register(Visit, VisitAdmin)  # Correct registration of the Visit model with VisitAdmin
