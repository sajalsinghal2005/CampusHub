from django.db import models
from django.conf import settings

class Student(models.Model):

    user  =  models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    branch = models.CharField(max_length=100, blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )

    phone = models.CharField(max_length=15, blank=True, null=True)
    github = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True,null=True)

    resume = models.FileField(
        upload_to = "resumes/",
        blank = True,
        null=True
    )

    def __str__(self):
        return self.user.full_name