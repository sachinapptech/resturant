# from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Sum
from django.conf import settings

class Cuisine(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    views = models.IntegerField(null=True, blank=True,default=0)

    def __str__(self):
        return self.name or "Unnamed Cuisine"


class CuisinePhoto(models.Model):
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="cuisine_photos/", null=True, blank=True)

    def __str__(self):
        return f"Photo for {self.cuisine.name if self.cuisine else 'Unknown Cuisine'}"



class VisitorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255, null=True, blank=True)
    place = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    preferred_cuisine = models.ForeignKey(
        'Cuisine',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="preferred_by_visitors"
    )

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.get_full_name() or self.user.username  
        if not self.email:
            self.email = self.user.email
        if not self.place:
            self.place = self.user.place 
        
        if not self.contact_info:
            self.contact_info = self.user.phone_number

        super(VisitorProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.name or self.user.username

class Visit(models.Model):
    visitor = models.ForeignKey(VisitorProfile, on_delete=models.CASCADE, related_name="visits")
    cuisine = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True, blank=True, related_name="ordered_visits")
    
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="Rating between 0.0 and 5.0")
    visit_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Visit by {self.visitor.name} on {self.visit_date}"

    @classmethod
    def total_visits(cls, visitor):
        return cls.objects.filter(visitor=visitor).count()

    @classmethod
    def total_expenses(cls, visitor):
        return cls.objects.filter(visitor=visitor).aggregate(total=Sum('expense'))['total'] or 0

    @classmethod
    def cuisines_ordered(cls, visitor):
        cuisines = cls.objects.filter(visitor=visitor).values_list("cuisine__name", flat=True).distinct()
        return list(cuisines)
