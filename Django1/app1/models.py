from django.db import models
from django.contrib.auth.models import User

# one to one
class Person(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    address=models.TextField(max_length=100)

    def __str__(self):
        return self.first_name


    
class fav_color(models.Model):
    user=models.ManyToManyField(User)
    color=models.CharField(max_length=30)

    def chosen_by(self):
        return ",".join([str(p) for p in self.user.all()])