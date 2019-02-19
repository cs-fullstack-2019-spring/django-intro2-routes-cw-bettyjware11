from django.shortcuts import render

# Create your views here.
# Defining function to be called when the url is requested
from django.http import HttpResponse


# this function will return "Here you go! Cute Heels!" when called
def gogetthegood(request):
    return HttpResponse("Here you go! Cute Heels!")


# this function will return "Never liked this show!" when called
def happyhappyjoyjoy(request):
    return HttpResponse("Never liked this show!")
