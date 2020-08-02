from django.shortcuts import render, HttpResponse
import random
# Create your views here.

def index(request):
    return render(request,"generator/index.html")

def password(request):
    if request.method == "GET":
        characters =  list('abcdefghijklmnopqrstuvwxz')
        if request.GET.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if request.GET.get('number'):
            characters.extend(list('1234567890'))
        if request.GET.get('special'):
            characters.extend(list('~!@#$%^&*_'))
        length = int(request.GET.get('length'))
        generated_password = ""
        for i in range(length):
            generated_password += random.choice(characters)
    return render(request,"generator/password.html",{"generated_password":generated_password})