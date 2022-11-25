from django.db.models.signals import post_save
from django.contrib.auth.models import User  # -> Sender
from django.dispatch import receiver  # -> Signal Reciver
from .models import Profile


# When the User i saved to db (post_save), then reciver activate create_profile function.
# The function takes as paramter sender -> User, instance -> instance of User, created -> true when object created
# If User created the create Profile with the instance of User class
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# When  the instance of User is changed then also save a profile to db
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
