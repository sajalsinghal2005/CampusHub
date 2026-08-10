from django.db import models
from django.conf import settings
from companies.models import Company

class Application(models.model):

    class Status(models.TextChoices):
        PENDING = "PENDING","pending"
        SHORTLISTED = "SHORTLISTED" , "Short"
        REJECTED = "REJECTED","Rejected"
        SELECTED = "SELECTED","Selected"

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    status = models.CharField(
        max_length = 20,
        choices = Status.choices,
        default = Status.PENDING
        )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.company.name}"
