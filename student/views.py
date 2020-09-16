from django.shortcuts import render, redirect
from student.models import Student
from student.forms import StudentForm
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings


# Create your views here.

def add_students(request):
    if request.method=='POST':
        form = StudentForm(request.POST,request.FILES)
        #form.picture = form.cleaned_data["picture"]
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Form Submit success.')
            return redirect('/home')
    else:
        form = StudentForm()
    return render(request,'add_student.html',{'form':form})

def home(request):
    students= Student.objects.all()
    return render(request,'show.html',{'students':students})

def delete(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    messages.add_message(request, messages.WARNING, 'Student delete Success.')
    return redirect('/home')

def edit(request,id):
    student = Student.objects.get(id=id)
    return render(request,'edit.html',{'student':student})

def update(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Student updated Success.')
        return redirect('/home')
    return render(request,'edit.html',{'stundent':student})


def detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'details.html', {'student': student})

def sendMail(request):
    if request.method=='POST':
        to_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [to_email]
        send_mail(subject, message, email_from, recipient_list)
        messages.add_message(request, messages.SUCCESS, 'Mail Send Successful.')
        return redirect('/mail')
    return render(request, 'sendmail.html')


def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        messages.add_message(request, messages.SUCCESS, 'Login Failed.')
    return render(request,'login.html')











