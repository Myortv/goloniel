from django.db import models
# from django.contrib.auth.models import User
from account.models import User


class Credits(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True
        ordering = ['created']

    def __str__(self):
        return self.title + " | " + str(self.pk)
