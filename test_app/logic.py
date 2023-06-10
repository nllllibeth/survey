import random
import string
from .models import Test_form, Question

def create_login():
    characters = string.ascii_letters
    login = ''.join(random.choice(characters) for i in range(10))
    return login

def check_answers(request):
    total = 0
    correct = 0
    answers = []
    for q in request.POST:
        if q == 'csrfmiddlewaretoken':
            continue 
        question = Question.objects.get(id = q)
        answers.append(request.POST[q])
        total += 10
        if request.POST[q] == question.correct_answer:
            correct += 10
    return total, correct, answers

def add_attrs(request, id, login):
    testObj = Test_form.objects.get(login = login, test_id = id)
    total, correct, answers = check_answers(request)
    percent = correct / total * 100
    
    testObj.correct = correct
    testObj.save()
    testObj.total = total
    testObj.save()
    testObj.percent = percent
    testObj.save()
    testObj.answers = answers
    testObj.save()
    time = testObj.created

    return total, correct, percent, time
