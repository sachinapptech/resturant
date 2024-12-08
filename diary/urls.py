from django.urls import path

from .import views


urlpatterns = [
    path('user/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('restaurants/',views.getResturants,name="restaurants"),
    path('restaurant/<int:pk>/',views.getResturant,name="restaurant"),
]

