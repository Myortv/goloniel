from django.db import models
from account.models import User


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    content = models.TextField(blank=True, null=True)

    master = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True)


class Master(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    content = models.TextField(blank=True, null=True)
    rating = models.OneToOneField('MasterRatingModel', on_delete=models.CASCADE)
    group = models.CharField(max_length=100)

    is_active = models.BooleanField(default=False)


class MasterRatingModel(models.Model):

    likes = models.ManyToManyField(User)
    # dislikes = ManyToManyField(User)
