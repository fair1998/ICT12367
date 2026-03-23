from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
       all_Person = Person.objects.all()
       return render(request, "index.html" , {"all_Person": all_Person})

def form(request):
    return render(request, "form.html")

def about(request):
      return render(request, "about.html")