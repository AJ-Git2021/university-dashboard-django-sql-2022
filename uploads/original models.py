
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


# changes after here
# class Course(models.Model):
#     course_id = models.DecimalField(primary_key=True,max_digits=10,decimal_places=0)
#     course_name = models.CharField(max_length=256)
#     course_duration =  models.DecimalField(max_digits=10,decimal_places=0)
#     def __str__(self):
#         return str(self.course_id)

# class Student(models.Model):
#     sap = models.DecimalField(primary_key=True,max_digits=16,decimal_places=0)
#     name  = models.CharField(max_length=256)
#     course_id = models.DecimalField(max_digits=10,decimal_places=0)
#     def __str__(self):
#         return str(self.sap)

# class Subject(models.Model):
#     subject_id = models.DecimalField(primary_key=True,max_digits=10,decimal_places=0)
#     subject_credits =  models.DecimalField(max_digits=10,decimal_places=0)
#     course_id = models.CharField(max_length=256)
#     def __str__(self):
#         return str(self.subject_id)

