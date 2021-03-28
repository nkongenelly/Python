from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QuestionForms
from .services import getQuestions

categories = ["Any Category", "General Knowledge", "Science & Nature", "Science: Mathematics", "Science: Computer", "Geography", "History", "Politics", "Art", "Animals"]
difficulty = ["Any Difficulty", "easy", "Medium", "hard"]
category = ""
level = ""
def home(request):
    context = {
        "categories": categories,
            "difficulty": difficulty
        }
    if request.method == 'POST':
        category1 = request.POST
        formValues = QuestionForms(request.POST)
        if formValues.is_valid():
            category = formValues.cleaned_data.get("category")
            level = formValues.cleaned_data.get("level")
            questions = getQuestions()
            print("category = ", category)
            print("level = ", level)
            print("formValues = ", formValues)
            print("getQuestions1 = ", questions)
            return render(request, 'questions/questions.html', {'form': formValues, 'questions' : questions}) 

    else :
        formValues = QuestionForms()
        context['form']=formValues
        #     return render(request, 'questions/home.html', {'form': formValues})
    return render(request, 'questions/home.html', {'form': formValues})

# def questions(request):
#     context = {
#         'questions' : getQuestions()
#     }
#     return render(request, 'questions/questions.html', context)
