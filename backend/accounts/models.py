from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class Role(models.TextChoices):
        STUDENT = "STUDENT","Student"
        PLACEMENT = "PLACEMENT","Placement"
        ADMIN = "ADMIN","Admin"

    full_name = models.CharField(max_length=100)
    emails = models.EmailField(unique=True)
    role = models.CharField(
        max_length = 20,
        choices = Role.choices,
        default = Role.STUDENT
    )

    EMAIL_FIELD = "emails"
    USERNAME_FIELD = "emails"

    REQUIRED_FIELDS = ["username","full_name"]