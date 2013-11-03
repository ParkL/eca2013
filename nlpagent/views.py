from django.http import HttpResponse
from django.template import RequestContext, loader # FIXME remove me
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello World!")

def echo(request):
    try:
        msg = request.POST['message']
    except KeyError:
        msg = ''
    return render(request, 'nlpagent/echo.html', {'message' : msg})