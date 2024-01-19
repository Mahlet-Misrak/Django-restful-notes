# models.py (inside the user app)
from django.db import models
from django.contrib.auth.models import User as DjangoUser

class UserProfile(models.Model):
    # user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    # Add any additional fields for the UserProfile model as needed
    firstname = models.TextField(null=True, blank=True)
    lastname = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'user_table'
        app_label = 'user'

    def __str__(self):
        return self.user.username
