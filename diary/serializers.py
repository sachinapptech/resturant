from rest_framework import serializers
from .models import (
    Restaurant,RestaurantPhoto,Review,Cuisine,CuisinePhoto,VisitorProfile,Visit
)

class RestaurantSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)
    total_reviews = serializers.IntegerField(read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
    
    def validate(self,data):
        opening_time = data.get('opening_time')
        closing_time = data.get('closing_time')

        if opening_time and closing_time and opening_time >= closing_time:
            raise serializers.ValidationError('Opening time must be earlier than closing time')
        
        return data

class RestaurantPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantPhoto
        fields = '__all__'

    def validate_photo(self,value):
        if value > 5 * 1024 * 1024 :
            raise serializers.ValidationError('Image size must not exceed 5MB')
        return value
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self,value):
        if value < 0.0 or value > 5.0:
            raise serializers.ValidationError('Rating must be between 0.0 and 5.0') 
        return value

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine 
        fields = '__all__'
    
    def validate_price(self,value):
        if value < 0:
            raise serializers.ValidationError('Price cannot be negative')
        return value
    
    def vaidate_name(self,value):
        if not value.strip():
            raise serializers.ValidationError('Cuisine name cannot be empty')
        return value


class CuisinePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuisinePhoto
        fields = '__all__'
    
    def validate_photo(self,value):
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError('Image size must not be exceed 5 MB')
        return value

class VisitorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorProfile
        fields = '__all__'
    
    def validate_contact_info(self,value):
        if value and len(value) < 10:
            raise serializers.ValidationError('Contact Info must be at least 10 charactor')
        return value


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit 
        fields = '__all__'
    
    def validate_expense(self,value):
        if value < 0:
            raise serializers.ValidationError('Expense cannot be negative')
        return value
    
    def validate_rating(self,value):
        if value < 0.0 or value > 5.0:
            raise serializers.ValidationError('Rating must be between 0.0 and 5.0')
    
    # def validate(self,data):
    #     if not data.get('comment'):
    #         raise serializers.ValidationError('Comment field cannot be empty')
    #     return data