from django import forms

class QuestionForms(forms.Form):
    CATEGORIES = (("Any Category", "Any Category"),("General Knowledge", "General Knowledge"), ("Science & Nature", "Science & Nature"), ("Science: Mathematics", "Science: Mathematics"),
     ("Science: Computer", "Science: Computer"), ("Geography", "Geography"), ("History", "History"), ("Politics", "Politics"), ("Art", "Art"), ("Animals", "Animals"))
    category = forms.ChoiceField(choices=CATEGORIES)
    LEVELS = (("Any Difficulty", "Any Difficulty"), ("easy", "easy"), ("Medium", "Medium"), ("hard", "hard"))
    level = forms.ChoiceField(choices=LEVELS)

    class Meta:
        fields = ["category", "level"]

# class Question(forms.Form):
