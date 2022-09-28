from django.shortcuts import render
from django.http import HttpResponse
from .models import PLACE, TEAM

# Create your views here.
# def place(request):
#    return render(request,"index.html")
def demo(request):
    obj = PLACE.objects.all()
    obj1 = TEAM.objects.all()
    return render(request,"index.html",{'result': obj, 'result1' : obj1})








