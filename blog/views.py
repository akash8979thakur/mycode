from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('this is blogHome .  ')



def blogPost(request, slug):
    return HttpResponse(f'this is blogPost:{slug} ')    