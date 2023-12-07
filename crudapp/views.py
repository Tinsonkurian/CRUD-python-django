from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def index(request):
    dict_emp = {
        'emp': Employee.objects.all()
    }
    return render(request, 'index.html', dict_emp)

def adduser(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']

        emp = Employee(
            name=name,
            email=email,
            age=age,
        )
        emp.save()
        print("created successfully")
        return redirect('/')
    return render(request, 'adduser.html')

def edituser(request,id):
    dict_emp = {
        'emp': Employee.objects.get(id=id)
    }
    return render(request, 'edituser.html', dict_emp)

def updateuser(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']

        emp = Employee.objects.get(id=id)
        emp.name = name
        emp.email = email
        emp.age = age

        emp.save()
        return redirect('/')


def deleteuser(request,id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')
