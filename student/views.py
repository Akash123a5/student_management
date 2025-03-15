from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages

# Create your views here.

def index(request):
    StudentS = Student.objects.all()
    context = {
        'students': StudentS
    }
    return render(request, 'index.html', context)

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']

        student = Student(name=name, email=email, phone=phone, course=course)
        student.save()
        messages.success(request, "Student added successfully!")
        return render(request, 'addstudent.html')
    else:

     return render(request, 'addstudent.html')
    

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.error(request, "Student deleted successfully!")
    return redirect('index')


def edit_student(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'edit_student.html', context)


def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.course = request.POST.get('course')
        
        student.save()  # বর্তমান অবজেক্ট আপডেট করে সংরক্ষণ করা হলো
        messages.success(request, "Student updated successfully!")
        return redirect('index')  # নিশ্চিত করুন 'index' নামে URL রয়েছে

    return render(request, 'edit_student.html', {'student': student})




