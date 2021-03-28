from django import forms
from .services import getQuestions

class QuestionForms(forms.Form):
    CATEGORIES = (("Any Category", "Any Category"),("General Knowledge", "General Knowledge"), ("Science & Nature", "Science & Nature"), ("Science: Mathematics", "Science: Mathematics"),
     ("Science: Computer", "Science: Computer"), ("Geography", "Geography"), ("History", "History"), ("Politics", "Politics"), ("Art", "Art"), ("Animals", "Animals"))
    category = forms.ChoiceField(choices=CATEGORIES)
    LEVELS = (("Any Difficulty", "Any Difficulty"), ("easy", "easy"), ("Medium", "Medium"), ("hard", "hard"))
    level = forms.ChoiceField(choices=LEVELS)

    class Meta:
        fields = ["category", "level", "questionId", "question", "answer1", "answer"]

class QuestionListForms(forms.Form):
    QUESTIONS = []
    allQuestions = getQuestions()
    for question in allQuestions:
        QUESTIONS.append(question)
        formQuestion  = forms.CharField(max_length=100)

    # class Meta:
    #     fields = ["question", "answer"]

