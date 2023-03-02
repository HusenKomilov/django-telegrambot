from django.db import models


# Create your models here.
class BotUser(models.Model):
    user_id = models.CharField(max_length=120, unique=True, verbose_name="Chat_id")
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=100, null=True, blank=True)
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Feedback(models.Model):
    user_id = models.CharField(max_length=120)
    created_ad = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.user_id
