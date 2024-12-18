from django.urls import path
from .views import (
    RestaurantListCreateView, RestaurantDetailView, RestaurantReviewsView, RestaurantPhotosView,
    CuisineListCreateView, CuisineDetailView, CuisinePhotosView,
    VisitorProfileListCreateView, VisitorProfileDetailView,
    VisitListCreateView, VisitDetailView,
    ReviewListCreateView, ReviewDetailView
)

urlpatterns = [
    # Restaurant URLs
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/reviews/', RestaurantReviewsView.as_view(), name='restaurant-reviews'),
    path('restaurants/<int:pk>/photos/', RestaurantPhotosView.as_view(), name='restaurant-photos'),

    # Cuisine URLs
    path('cuisines/', CuisineListCreateView.as_view(), name='cuisine-list'),
    path('cuisines/<int:pk>/', CuisineDetailView.as_view(), name='cuisine-detail'),
    path('cuisines/<int:pk>/photos/', CuisinePhotosView.as_view(), name='cuisine-photos'),

    # Visitor Profile URLs
    path('profiles/', VisitorProfileListCreateView.as_view(), name='visitor-profile-list'),
    path('profiles/<int:pk>/', VisitorProfileDetailView.as_view(), name='visitor-profile-detail'),

    # Visit URLs
    path('visits/', VisitListCreateView.as_view(), name='visit-list'),
    path('visits/<int:pk>/', VisitDetailView.as_view(), name='visit-detail'),

    # Review URLs
    path('reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
