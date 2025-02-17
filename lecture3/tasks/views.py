from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

#tasks =[]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #intfield=forms.IntegerField(label="Input Integer",min_value=1, max_value=99 )

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    #return render(request, "tasks/index.html",{ "tasks":tasks })
    return render(request, "tasks/index.html",{ "tasks":request.session["tasks"] })

def add(request):
    if request.method =="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            #tasks.append(task)
            request.session["tasks"] +=[task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{ "form":form })            
    return render(request,"tasks/add.html",{ "form":NewTaskForm() })


