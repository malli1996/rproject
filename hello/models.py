from django.db import models

# Create your models here.
class Student(models.Model):
        student_id = models.IntegerField()
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        address = models.CharField(max_length=30)

