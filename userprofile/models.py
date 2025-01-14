from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import TimeStampedUUIDModel

User = get_user_model()

class Gender(models.TextChoices):
    MALE = "Male",_("Male")
    FEMALE = "Female",_("Female")
    OTHER = "Other",_("Other")


class UserProfile(TimeStampedUUIDModel):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    profile_photo = models.ImageField(verbose_name=_("profile Photo"),default="/profile_default.png")
    gender = models.CharField(verbose_name=_("Gender"),choices=Gender.choices,default=Gender.OTHER,max_length=20)
    place = models.CharField(verbose_name=_("Place"),max_length=180,blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

