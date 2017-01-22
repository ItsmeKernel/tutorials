from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    teacher = models.ForeignKey(Teacher)

    def __str__(self):
        return self.name
