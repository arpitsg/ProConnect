from turtle import pos
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,Relationship

@receiver(post_save,sender=User)
def postSaveCreateProfile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    # print("posted",instance.status)
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'Accepted':
        print('adding')
        sender_.connections.add(receiver_.user)
        receiver_.connections.add(sender_.user)
        sender_.save()
        receiver_.save()
