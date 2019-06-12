from django.shortcuts import render, HttpResponse

from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    output = " ".join([q.question_text for q in latest_questions])
    response = f"This is a list of latest question: {output}"
    return HttpResponse(response)

def detail(request, question_id):
    response = f"You're looking at question {question_id}"
    return HttpResponse(response)

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    response = f"You're voting on question {question_id}"
    return HttpResponse(response)