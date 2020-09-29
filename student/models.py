from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    section = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name
