from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'bookin/login.html')
def register(request):
   return HttpResponse(render(request, 'bookin/register.html'))
def relog(request):
   return HttpResponse(render(request, 'bookin/login.html'))
def order(request):
   return HttpResponse(render(request, 'bookin/order.html'))
def info(request):
   return HttpResponse(render(request, 'bookin/info.html'))
