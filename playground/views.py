from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
  # dummy variables
    x = 1
    y = 2
    # manual
    # return HttpResponse('hi')
    # shwow hello world as a header template
    return render(request, 'hello.html', {'name': 'El'})
