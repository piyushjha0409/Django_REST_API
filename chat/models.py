from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#modal for the user
# class Users(models.Model):
#     username = models.TextField(),
#     email = models.TextField(),
#     password = models.TextField()

#Model for the message
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    content = models.TextField(),
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50] #message should not be more than 50 characters



