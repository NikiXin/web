from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def detail(request,question_id):
	return HttpResponse("You are looking at question %s" % question_id)

def results(request,question_id):
	response = " you are looking at the resuls of question %s"
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse("you are voting on question %s." %question_id)