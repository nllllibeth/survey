from django.shortcuts import render
from .models import Test_form, Test, Question
from .logic import *

# Create your views here.

def home(request):
    login = create_login()
    context = {
        'login' : login,
    }
    return render(request, 'test_app/home.html', context)

def create(request, login):
    iq_test = Test.objects.get(name = 'IQ')
    eq_test = Test.objects.get(name = 'EQ')
    context = {
        'iq_test' : iq_test,
        'eq_test' : eq_test,
        'login' : login,
    }
    return render(request, 'test_app/create.html', context)

def vote(request, id, login):
    test = Test.objects.get(id = id)
    testObj = Test_form(
        test_id = Test.objects.get(id=id),
        login = login)
    testObj.save()
    questions = Question.objects.all().filter(test_id = test)

    context = {
        'id' : id,
        'login' : login,
        'test' : testObj,
        'questions' : questions,
    }
    return render(request, 'test_app/vote.html', context)

def get_results(request, id, login):
    if request.method == "POST":
        total, correct, percent, time = add_attrs(request, id, login)

    context = {
        'login' : login,
        'total' : total,
        'correct' : correct,
        'percent' : percent,
        'time' : time,
    }
    return render(request, 'test_app/results.html', context)


def get_results_page(request):
    return render(request, 'test_app/results_page.html')

def get_scores(request):
    if request.method == 'POST':
        testObjs = Test_form.objects.all().filter(login = request.POST['login'])
    context = {
        'objs' : testObjs,
    }
    return render(request, 'test_app/scores.html', context)