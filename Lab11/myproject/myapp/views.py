from django.shortcuts import render , redirect
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
       all_Person = Person.objects.all()
       return render(request, "index.html" , {"all_Person": all_Person})

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        person = Person.objects.create(name=name , age=age)
        return redirect("/")
    else:
        return render(request, "form.html")

def about(request):
      return render(request, "about.html")