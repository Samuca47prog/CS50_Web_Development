from logging import PlaceHolder
from django.shortcuts import render
from django import forms

from . import util

import markdown

class Query(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={'class': 'search'}), label="")

def index(request):
    # if user has POSTed something, render a list of possible pages to get in
    # else, render the index page
    if request.method == "POST":
        form = Query(request.POST)
        if form.is_valid():
            q = form.cleaned_data["q"]
            return queryResponse(request, q)
    else:
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
    
# answer user query in the search box
def queryResponse(request, q):
    entries = util.list_entries()
    entries.remove("notFound")

    substring_entries = []

    for entry in entries:
        # if user have typed page exacly name
        if q == entry:
            return renderPage(request, q)
        # append results of pages that contains the query
        if q.lower() in entry.lower():
            substring_entries.append(entry)
    
    return render(request, "encyclopedia/queryResponse.html", {
        "entries": substring_entries,
        "q": q
    })