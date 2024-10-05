from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = ArrayField(models.CharField(max_length=50), blank=True, default=list)

    def __str__(self) -> str:
        return f"Skills - {self.user.name}"

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    work_phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"Contact - {self.user.name}"
