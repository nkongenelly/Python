from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QuestionForms

categories = ["Any Category", "General Knowledge", "Science & Nature", "Science: Mathematics", "Science: Computer", "Geography", "History", "Politics", "Art", "Animals"]
difficulty = ["Any Difficulty", "easy", "Medium", "hard"]
category = ""
level = ""
def home(request):
    context = {
        "categories": categories,
            "difficulty": difficulty
        }
    print("request.method = ", request.method)
    if request.method == 'POST':
        category1 = request.POST
        print("categoriessss = ", category1)
        formValues = QuestionForms(request.POST)
        print("formValues.is_valid() = ", formValues.is_valid())
        if formValues.is_valid():
            category = formValues.cleaned_data.get("category")
            level = formValues.cleaned_data.get("level")
            print("category = ", category)
            print("level = ", level)
            return render(request, 'questions/questions.html', {'form': formValues}) 

    else :
        formValues = QuestionForms()
        context['form']=formValues
        #     return render(request, 'questions/home.html', {'form': formValues})
    return render(request, 'questions/home.html', {'form': formValues})

def questions(request):
    print("request.method 2= ", request.method)
    return render(request, 'questions/questions.html')
