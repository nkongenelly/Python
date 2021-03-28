import os
import requests

def getQuestions():
    url = "https://opentdb.com/api.php?amount=10"
    # https://opentdb.com/api.php?amount=10&category=9&difficulty=easy
    r = requests.get(url)
    questions = r.json()
    question_list = questions['results']
    return question_list

