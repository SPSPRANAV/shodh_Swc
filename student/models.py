from django.db import models

# Create your models here.
class Intern_Model(models.Model):
    department_name=models.CharField(max_length=5)
    prof_name=models.CharField(max_length=100)
    min_cpi=models.FloatField()
    title=models.CharField(max_length=50)
    skills=models.TextField(max_length=100)
    description=models.TextField(max_length=500)
    def __str__(self):
        return self.prof_name + '-' + self.department_name + '  Department'
class User_profile(models.Model):
    user_name=models.CharField(max_length=100)
    user_cpi=models.FloatField()
    user_branch=models.CharField(max_length=5)
    def __str__(self):
        return self.user_name
class Applyform(models.Model):
    cv=models.FileField()
    bio = models.TextField(blank=True)
