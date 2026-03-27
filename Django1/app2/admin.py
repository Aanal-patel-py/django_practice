from django.contrib import admin
from app2.models import Student,Clubs

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age','classname','marks')
@admin.register(Clubs)
class ClubAdmin(admin.ModelAdmin):
    list_display=('name','chosen_by')
