from django.db import models


# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class SubService(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    value = models.IntegerField()
    required = models.BooleanField()
    many = models.BooleanField()
    skills = models.ManyToManyField(Skill, related_name="project")

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    sub_service = models.ManyToManyField(SubService, related_name="sub_service")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    service = models.ManyToManyField(Service, related_name="service")

    def __str__(self):
        return self.name
