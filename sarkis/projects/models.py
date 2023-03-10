from django.db import models
from skills.models import SubService, Skill


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    sub_services = models.ManyToManyField(SubService, related_name="sub_services")
    skill = models.ManyToManyField(Skill, related_name="skill")
    link = models.CharField(max_length=50, null=True, blank=True)
    github = models.CharField(max_length=50, null=True, blank=True)
    goal = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='image.jpg')

    def __str__(self):
        return self.name

    @property
    def get_skills(self):
        list = []
        for i in self.skill.all():
            list.append(i)
        return list

    @property
    def get_sub_services(self):
        list = []
        for i in self.sub_services.all():
            list.append(i)
        return list


