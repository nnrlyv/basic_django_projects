from datetime import timezone

from django.contrib.messages import success
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from polls.models import Question, Choice
from .forms import QuestionForm


# list of questions takes latest 5 ques
def index(request):
    latest_questions = Question.objects.filter(is_ready=True).order_by("-published_date")[:5]
    return render (request,"polls/index.html", {"latest_questions": latest_questions})

#страница вопроса с формой голосования
def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    question.views_count += 1
    question.save()
    return render(request , "polls/detail.html", {"question": question})

#for voting with POST
def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    is_ready = True
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        #if person didnt choose anything
        return render(request, "polls/detail.html", {"question":question})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #after POST always redirect
        return HttpResponseRedirect(reverse("polls:results", args = (question_id,)))

#для вывода результатов
def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, "polls/results.html", {"question":question})

def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = QuestionForm()
    return render(request, "polls/add_question.html")


