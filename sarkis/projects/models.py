from django.db import models
from skills.models import SubService, Skill


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    sub_services = models.ManyToManyField(SubService, related_name="sub_services")
    skill = models.ManyToManyField(Skill, related_name="sub_services")

    def __str__(self):
        return self.name
