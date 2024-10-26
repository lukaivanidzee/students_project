from django.shortcuts import render
import random

def random_students():
    students = []
    for _ in range(100):
        student = {
            'name': random.choice(["Luka", "Nino", "Dato", "Gurama", "Zaka", 'Mamuka']),
            'surname': random.choice(["Ivanidze", "Beglarishvili", "Mkervalishvili", "Xazaradze", "Shavyverasshvili"]),
            'gpa': round(random.uniform(1.0, 4.0), 2),
            'course': random.randint(1, 4)
        }
        students.append(student)
    return students

def main_page_view(request):
    students = random_students()
    student = random.choice(students)
    return render(request, 'students/main_page.html', {'student': student})

def students_page_view(request):
    students = random_students()
    return render(request, 'students/students_page.html', {'students': students})
