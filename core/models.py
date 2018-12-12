import uuid
import random

from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework.compat import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator


class EducationalOpportunityManager(models.Manager):
    @staticmethod
    def create_random(activity: str, submit=True):
        scales = [random.randint(0, 100) for _ in range(6)]
        educational_opportunity = EducationalOpportunity(scales=scales, activity=activity)
        if submit:
            educational_opportunity.save()
        return educational_opportunity


class EducationalOpportunity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    scales = ArrayField(size=6, validators=[MinLengthValidator(6), MinLengthValidator(6)],
                        base_field=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)]))
    activity = models.CharField(max_length=50)

    objects = EducationalOpportunityManager()
