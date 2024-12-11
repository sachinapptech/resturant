from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import VisitorProfile

@receiver(pre_save, sender=User)
def updateUser(sender,instance,**kwargs):
    user = instance
    if user.email != '':
        user.username = user.email



@receiver(post_save, sender=User)
def create_or_update_visitor_profile(sender, instance, created, **kwargs):
    if created:
        VisitorProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'VistorProfile'):
            instance.profile.save()