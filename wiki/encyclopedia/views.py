from django.shortcuts import render
from . import utils

# Create your views here.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": utils.list_entries()
    })
