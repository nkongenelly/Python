from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QuestionForms, QuestionListForms
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
        # if(request.POST['answer']):
        #     answer = request.POST['answer']
        results = dict(request.POST)
        print("answersssss = ", request.POST)
        # for result in results.get("question") :
        print("answersssss1 = ", [results.get("question")])
        print("answersssss = ", [results.get("answer")])
        print("answersssss = ", [results.get("answer1")])
        print("answersssss = ", ([results.get("answer")] in [results.get("question")]))
        print("answersssss = ", ([results.get("answer1")] in [results.get("question")]))
        formValues = QuestionForms(request.POST)
        if formValues.is_valid():
            category = formValues.cleaned_data.get("category")
            level = formValues.cleaned_data.get("level")
            id = results.get("question")
            # id = request.data.get("question")
            questions = getQuestions()
            print("category = ", category)
            print("level = ", level)
            if (formValues.cleaned_data.get("answer")):
                answer = formValues.cleaned_data.get("answer")
                print("answerssss1 = ", answer)
            print("formValues = ", formValues)
            print("getQuestions1 = ", questions)
            print("idddd1 = ", id)
            return render(request, 'questions/questions.html', {'form': formValues, 'questions' : questions}) 
            

    else :
        formValues = QuestionForms()
        context['form']=formValues
        #     return render(request, 'questions/home.html', {'form': formValues})
    return render(request, 'questions/home.html', {'form': formValues})

def questions(request):
    if request.method == 'POST':
        category1 = request.POST
        formValues = QuestionListForms(request.POST)
        if formValues.is_valid():
            question = formValues.cleaned_data.get("question")
            answer = formValues.cleaned_data.get("answer")
            questions = getQuestions()
            print("question = ", question)
            print("answer = ", answer)
            return render(request, 'questions/questions.html', {'form': formValues, 'questions' : questions}) 

    else :
        formValues = QuestionListForms()
    return render(request, 'questions/questions.html', {'form': formValues})
