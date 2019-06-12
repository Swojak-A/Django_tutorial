from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    context = {
        "latest_question_list": latest_questions,
    }

    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {
        "question": question
    }
    response = f"You're looking at question {question_id}"

    return render(request, "polls/detail.html", context)

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    response = f"You're voting on question {question_id}"
    return HttpResponse(response)