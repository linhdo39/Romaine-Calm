from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if Profile.objects.filter(user=instance).exists():
        Profile.objects.get(user=instance).save()
    else:
        profile = Profile (
            user = instance,
            bio = ""
        )
        profile.save();
