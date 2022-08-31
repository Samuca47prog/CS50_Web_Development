from django.shortcuts import render

from . import util

import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def renderPage(request, name):
    entries = list(map(lambda x: x.lower(), util.list_entries()))
    if name not in entries:
        name = "notFound"
    return render(request, "encyclopedia/renderPage.html", {
        "page": markdown.markdown(util.get_entry(name)),
        "title": name
    })
    