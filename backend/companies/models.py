from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)

    logo = models.ImageField(
        upload_to = "company_logos/",
        blank = True,
        null = True
    )

    website = models.URLField(blank = True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    hr_email = models.EmailField()

    ctc = models.DecimalField(
        max_digits = 8,
        decimal_places = 2
    )

    minimum_cgpa = models.DecimalField(
        max_digits = 4,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name