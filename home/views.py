from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('this is home')

def about(request):
    return HttpResponse('this is about')

def contact(request):
    return HttpResponse('this is contact')



