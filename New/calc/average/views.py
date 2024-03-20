from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    x=list(map(int,input("list of inputs").split()))
    p=sum(x)//len(x)
    return HttpResponse("average ",p)
    return render(request,"calc.html")

# Create your views here.
