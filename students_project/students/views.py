import random
from django.shortcuts import render

def get_random_students():
    students = []
    for _ in range(100):
        student = {
            'name': random.choice(['Ana', 'Nino', 'JUmber', 'Shalva', 'Nodar', 'Dato', 'Deme']),
            'surname': random.choice(['Aloiani', 'Sekania', 'Kobakhidze', 'Natelashvili', 'Ivanidze', 'Oniani']),
            'gpa': round(random.uniform(1.0, 4.0), 2),
            'course': random.randint(1, 4)
        }
        students.append(student)
    return students

def main_page_view(request):
    students = get_random_students()
    random_student = random.choice(students)
    return render(request, 'main_page.html', {'student': random_student})

def students_page_view(request):
    students = get_random_students()
    return render(request, 'students_page.html', {'students': students})