from django.shortcuts import render

from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        util.save_entry(title, content)

        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": util.get_markdown(title)
        })
    
    else:

        if title in util.list_entries():
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": util.get_markdown(title)
            })
        
       
        return render(request, "encyclopedia/error.html", {
                "message": "Requested page was not found."
            })
    
def random_entry(request):
    entries = util.list_entries()

    if not entries:
        return render(request, "encyclopedia/error.html", {
            "message": "No entries found."
        })

    title = random.choice(entries)
    
    return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": util.get_markdown(title)
        })

def new_entry(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        entry_list = [entry.lower() for entry in util.list_entries()]

        if title.lower() in entry_list:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry already exists."
            })
        else:
            entry = f"# {title}\n\n{content}"
            util.save_entry(title, entry)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": util.get_markdown(title)
            })
    
    else:
        return render(request, "encyclopedia/new.html")
    
def edit(request):
    if request.method == "POST":
        title = request.POST.get("title")

        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": util.get_entry(title)
        })

def search(request):
    query = request.POST.get("q").lower().strip()
    entries = util.list_entries()
    results = [entry for entry in entries if query in entry.lower()]  
    
    if len(results) == 0:
        return render(request, "encyclopedia/error.html", {
            "message": "No results found."
        })
    
    elif len(results) == 1:
        title = results[0]
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": util.get_markdown(title)
        })

    else:
        return render(request, "encyclopedia/results.html", {
                        "entries": results
                        }
                )