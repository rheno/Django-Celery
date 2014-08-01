from django.shortcuts import render
from django.http import HttpResponse
from demoapp.tasks import add

# Create your views here.
def see_view(request):
  add.delay(10,10)
  return HttpResponse("<h1>MyCelery</h1>")
