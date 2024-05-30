from django.db import models
from django.contrib.auth.models import AbstractUser

class customeUser(AbstractUser):
    prfile_image = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)