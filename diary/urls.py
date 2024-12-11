from django.urls import path

from .import views

urlpatterns = [
    path('cuisines/', views.cuisine_list_create, name='cuisine-list-create'),
    path('cuisines/<int:pk>/', views.cuisine_detail_update_delete, name='cuisine-detail-update-delete'),

    path('visitor/', views.visitor_profile, name='visitor-profile'),

    path('visits/', views.visit_list_create, name='visit-list-create'),
    path('status/', views.visitor_status, name='visitor-status'),
]

