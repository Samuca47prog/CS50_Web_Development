from logging import PlaceHolder
from django.shortcuts import render
from django import forms

from . import util

import markdown

class Query(forms.Form):
    q = forms.CharField(label="Search..")

def index(request):
    if request.method == "POST":
        form = Query(request.POST)
        name = form.cleaned_data["q"]
        return renderPage(request, name)
    
    entries = util.list_entries()
    entries.remove("notFound")
    return render(request, "encyclopedia/index.html", {
        "entries": entries,
        "form": Query()
    })

def renderPage(request, name): 
    name = name.lower()
    entries = list(map(lambda x: x.lower(), util.list_entries()))
    if name not in entries:
        name = "notFound"
    return render(request, "encyclopedia/renderPage.html", {
        "page": markdown.markdown(util.get_entry(name)),
        "title": name
    })
    