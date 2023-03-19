from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, Http404
from django.utils.html import escape
from .models import Question, Answer, Contact

from django.template import loader

def index(request):
    # return HttpResponse(f"Hey You are in home, Your request : {escape(repr(request))}")
    quesList = Question.objects.all()
    return render(request, "home/index.html",{"quesList":quesList})


def ParticularQues(request, ques_id):
    # try:
    #     question = Question.objects.get(pk=ques_id)
    # except Question.DoesNotExist:
    #     raise Http404("The id does not exist")
    quest = get_object_or_404(Question,pk=ques_id)
    # return HttpResponse(f"This is partuclar questions and it's id is : {quest}")
    return render(request,"home/details.html",{"ques":quest})


def vote(request, ques_id):
    question = get_object_or_404(Question, pk=ques_id)
    selected_choice = question.choice_set.get(pk = request.POST['choice'])

    selected_choice.votes+=1
    selected_choice.save()

    ans = Answer.objects.create(question=question.question_text, ans=selected_choice.choice_text)
    ans.save()

    return HttpResponse("Hey")

def result(request, ques_id):
    question = get_object_or_404(Question, pk=ques_id)
    choices = question.choice_set.all()
    return render(request,"home/result.html", context={'ques':question.question_text, 'choices':choices})

def contact(request):

    if (request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        issue = request.POST['issue']

        contact = Contact(name=name, email = email, issue=issue)
        contact.save()

        return redirect("/")


    return render(request, "home/contact.html")