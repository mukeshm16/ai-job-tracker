from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected'),
    ]

    company_name = models.CharField(max_length=100)

    role = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    applied_date = models.DateField()

    notes = models.TextField()

    def __str__(self):
        return self.company_name