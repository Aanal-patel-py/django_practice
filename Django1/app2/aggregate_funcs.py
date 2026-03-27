from app2.models import Student,Clubs
from django.db import connection
from django.db.models import Avg, Max, Min, Count,Sum,F

def run():
    # print(Student.objects.aggregate(total_marks=Sum('marks')))
    x=Student.objects.filter(marks__gt=40).first()
    # x.marks+=1
    x.marks=F('marks')+1
    x.save()
    print(x)
    print(connection.queries)