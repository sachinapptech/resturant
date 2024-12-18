from django.contrib import admin
from .models import (Restaurant,RestaurantPhoto,Review,Cuisine,CuisinePhoto,VisitorProfile,Visit)


class RestaurantPhotoInline(admin.TabularInline):
    model = RestaurantPhoto
    extra = 1

class ReviewInline(admin.TabularInline):
    model = Review

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','city','average_rating','total_reviews','created_at','updated_at')
    search_fields = ('name','city','address')
    list_filter = ('city','cuisines')
    inlines = [RestaurantPhotoInline,ReviewInline]
    readonly_fields = ('average_rating','total_reviews')

    def average_rating(self,obj):
        return obj.average_rating()
    average_rating.short_description = 'Total Reviews'

class ResturantPhotoAdmin(admin.ModelAdmin):
    list_display = ('restaurant','photo','uploaded_at')
    list_filter = ('restaurant',)
    search_fields = ('restaurant__name',)

class ReviewAdmin(admin.ModelAdmin):
    list_display =('restaurant','visitor','rating','created_at')
    list_filter = ('rating','created_at')
    search_fields = ('restaurant__name','visitor__username','comment')

class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name','price','views')
    search_fields = ('name',)
    list_filter = ('views',)

class CuisinePhotoAdmin(admin.ModelAdmin):
    list_display = ('cuisine','photo')
    search_fields = ('cuisine__name',)

class VisitorProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name','email','place','preferred_cuisine')
    search_fields = ('user__username','name','email','place')
    list_filter = ('preferred_cuisine',)

class VisitAdmin(admin.ModelAdmin):
    list_display = ('visitor','cuisine','expense','rating','visit_date')
    list_filter = ('rating','visit_date')
    search_fields = ('visitor__name','cuisine__name','comment')

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(RestaurantPhoto,ResturantPhotoAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Cuisine,CuisineAdmin)
admin.site.register(CuisinePhoto,CuisinePhotoAdmin)
admin.site.register(VisitorProfile,VisitorProfileAdmin)
admin.site.register(Visit,VisitAdmin)
