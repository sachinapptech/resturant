from django.contrib import admin
from .models import Restaurant,Visit,CuisinePhoto

class CuisinePhotoInline(admin.TabularInline):
    model = CuisinePhoto
    extra = 1 
    fields = ('photo',)
    # readonly_fields = ('photo',)

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','place','cuisine_type','created_by')
    search_fields = ('name','place','cuisine_type')
    list_filter =('cuisine_type',)
    ordering = ('name',)
    inlines = [CuisinePhotoInline]

class VisitAdmin(admin.ModelAdmin):
    list_display = ('restaurant','visit_date','expense','rating')
    search_fields = ('restaurant__name',)
    list_filter = ('visit_date','rating','restaurant__cuisine_type')
    ordering = ('-visit_date',)
    date_hierarchy = 'visit_date'


admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Visit,VisitAdmin)



