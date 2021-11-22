from django.db import models

# Create your models here.
class UserImageDb(models.Model):
    name = models.CharField(max_length=120)
    user_image = models.ImageField(upload_to='user_image/')


    def __str__(self):
        return self.name