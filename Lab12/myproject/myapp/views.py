from django.shortcuts import render , redirect
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
       all_Person = Person.objects.all()
       return render(request, "index.html" , {"all_Person": all_Person})

def form(request, id=None):
    person = None
    if id:
        person = Person.objects.get(id=id)
    
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        
        if id:
            person.name = name
            person.age = age
            person.save()
        else:
            person = Person.objects.create(name=name , age=age)
        return redirect("/")
    else:
        return render(request, "form.html", {"person": person})

def about(request):
      return render(request, "about.html")

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect("/")