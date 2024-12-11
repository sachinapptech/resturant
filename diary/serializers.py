from rest_framework import serializers
from .models import Cuisine, CuisinePhoto, VisitorProfile, Visit

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = '__all__'


class CuisinePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuisinePhoto
        fields = '__all__'


class VisitorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorProfile
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
