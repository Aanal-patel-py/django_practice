from app2.models import Student

students = [
    Student(name="Rahul", age=20, classname="10", marks=85),
    Student(name="Amit", age=18, classname="12", marks=90),
    Student(name="Neha", age=19, classname="11", marks=88),
    Student(name="Priya", age=17, classname="10", marks=72),
    Student(name="Karan", age=21, classname="12", marks=65),
    Student(name="Sneha", age=20, classname="11", marks=95),
    Student(name="Arjun", age=18, classname="9", marks=40),
    Student(name="Pooja", age=19, classname="10", marks=30),
    Student(name="Vikas", age=22, classname="12", marks=55),
    Student(name="Anjali", age=17, classname="9", marks=25),
]
Student.objects.bulk_create(students)