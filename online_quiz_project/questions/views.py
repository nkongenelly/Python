from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'questions/home.html')

def questions(request):
    return render(request, 'questions/questions.html')
