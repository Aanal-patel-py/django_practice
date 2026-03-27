from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    classname=models.CharField(max_length=30)
    marks=models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.classname} - {self.marks}"
    
class Clubs(models.Model):
    students=models.ManyToManyField(Student)
    name=models.CharField(max_length=30)    

    class Meta:
        verbose_name="Club"

    def chosen_by(self):
        return ",".join(self.students.values_list('name',flat=True))


