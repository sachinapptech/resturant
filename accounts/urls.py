from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getAllUsers, name='get-all-users'), 
    path('create/', views.createUser, name='create-user'),  
    path('<int:pk>/', views.getUser, name='get-user'),
    path('<int:pk>/update/', views.updateUser, name='update-user'),
    path('<int:pk>/delete/', views.deleteUser, name='delete-user'),
]
