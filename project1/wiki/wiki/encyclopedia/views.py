from cProfile import label
from dataclasses import fields
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django import forms
import re
import random

from . import util

import markdown

class QuerySearch(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={'class': 'search'}), label="")

class NewPage(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 400px;', 'class': 'form-control'}))
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Body', 'style': 'width: 550px;', 'class': 'form-control'}))

class EditPage(forms.Form):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Body', 'style': 'width: 550px;', 'class': 'form-control'}))
    

def index(request):
    # if user has POSTed something, render a list of possible pages to get in
    # else, render the index page
    if request.method == "POST":
        form = QuerySearch(request.POST)
        if form.is_valid():
            q = form.cleaned_data["q"]
            return queryResponse(request, q)
    else:
        entries = util.list_entries()
        entries.remove("notFound")
        entries.remove("pageNameError")
        return render(request, "encyclopedia/index.html", {
            "entries": entries,
            "form": QuerySearch()
        })

def renderPage(request, name): 
    name = name.lower()
    entries = list(map(lambda x: x.lower(), util.list_entries()))
    if name not in entries:
        name = "notFound"
        return renderError(request, name)

    return render(request, "encyclopedia/renderPage.html", {
        "page": markdown.markdown(util.get_entry(name)),
        "title": name,
        "form": QuerySearch(),
    })

def renderError(request, name):
    return render(request, "encyclopedia/renderError.html", {
        "page": markdown.markdown(util.get_entry(name)),
        "title": name,
        "form": QuerySearch(),
    })
    
# answer user query in the search box
def queryResponse(request, q):
    entries = util.list_entries()
    entries.remove("notFound")
    entries.remove("pageNameError")

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
        "q": q,
        "form": QuerySearch()
    })

def createNewPage(request):
    # if user has POSTed something, save that entry
    # else, render create new page 
    if request.method == "POST":
        form = NewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]

            entries = util.list_entries()

            if title in entries:
                return renderError(request, "pageNameError")
            else:
                # save new page
                util.save_entry(title, body)
                return renderPage(request, title)
    else:
        return render(request, "encyclopedia/createNewPage.html", {
            "form": QuerySearch(),
            "content": NewPage()
        })

def editPage(request, name):
    if request.method == "POST":
        form = EditPage(request.POST)
        if form.is_valid():
            body = form.cleaned_data["body"]
            util.save_entry(name, body)
            return renderPage(request,name)
    else:
        form = EditPage(initial={'body': util.get_entry(name)})
        return render(request, "encyclopedia/editPage.html", {
                "title": name,
                "content": form,
            })



def randomPage(request):
    entries = util.list_entries()
    entries.remove("notFound")
    entries.remove("pageNameError")

    q = random.choice(entries)

    return renderPage(request, q)