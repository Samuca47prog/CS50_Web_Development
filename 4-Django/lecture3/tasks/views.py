from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request,"tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == 'POST':                                    # if user is trying to post the form
        form = NewTaskForm(request.POST)                            # take all the data from the form
        if form.is_valid():                                         # if form data is valid
            task = form.cleaned_data["task"]                        # get task field data
            request.session["tasks"] += [task]                                      # adds it to tasks list
            return HttpResponseRedirect(reverse("tasks:index"))     # loads index page
        else:                                                       # else, render user page again to they see what is wrong
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })