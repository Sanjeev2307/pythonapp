from django.shortcuts import render
from django.db import models
class user(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    cars = models.CharField(max_length=100)

class password_details(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



def main_view(request):
    name_input=request.GET.get('name')
    date_input=request.GET.get('date')
    cars_input=request.GET.get('cars')
    print('name',name_input,'date',date_input,'car',cars_input)
    if name_input and date_input and cars_input:
        # Assuming YourModel has fields name, date, and cars
        model_instance = user(name=name_input, date=date_input, cars=cars_input)
        model_instance.save()  # Save the model instance to the database
        users = user.objects.all()
    #return render(request,'index.html')
    return render(request, 'index.html', {'users': users})


def password_manager(request):
    Username_input=request.GET.get('Username')# Get user name from front end from input
    password_input=request.GET.get('password')# Get user password from front end from input
    if Username_input and password_input:
        new_user_passwordSave=password_details(username=Username_input,password=password_input) # data mapped in Django ORM
        new_user_passwordSave.save()# save the user password
    return render(request,'todo.html')