from django.shortcuts import render

from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):

    if title in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": util.get_entry(title)
        })
    
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "Requested page was not found."
        })
    
def random_entry(request):
    entries = util.list_entries()
    title = random.choice(entries)
    
    return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": util.get_entry(title)
        })