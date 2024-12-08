from django.contrib.auth.models import User
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    cuisine_type = models.CharField(max_length=255)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name= "restaurants")

    def __str__(self):
        return self.name

class CuisinePhoto(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="cuisine_photos")
    photo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return f"Photos for {self.restaurant.name}"


class Visit(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="visits")
    visit_date = models.DateField()
    expense = models.DecimalField(max_digits=10,decimal_places=2)
    note = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"Visit to {self.restaurant.name} on {self.visit_date}"