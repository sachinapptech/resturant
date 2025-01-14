from django.db.models.signals import post_save
from django.dispatch import receiver
from myproject.settings import AUTH_USER_MODEL
from userprofile.models import UserProfile

@receiver(post_save,sender=AUTH_USER_MODEL)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save,sender=AUTH_USER_MODEL)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
