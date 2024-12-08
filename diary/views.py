from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Restaurant
from .serializers import RestaurantSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)

        data['username'] = self.user.username
        data['email'] = self.user.email
        
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def getResturants(request):
    restaurants = Restaurant.objects.all()   
    serializer = RestaurantSerializer(restaurants,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getResturant(request,pk):
    try:
        restaurant = Restaurant.objects.get(id=pk)
    except Restaurant.DoesNotExist:
        return Response({'error':'Restaurant not found'},status=404)
    serializer = RestaurantSerializer(restaurant,many=False)
    return Response(serializer.data)



