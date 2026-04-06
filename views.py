from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to SecureVote Online Voting System")

def dashboard(request):
    return HttpResponse("Voting Dashboard")
