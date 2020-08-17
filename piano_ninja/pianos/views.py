from django.shortcuts import render
from django.http import HttpResponse
from .models import Pianos
from django.template import loader


def detail(request, rowid):
    piano = Pianos.objects.using("pianos").get(pk=rowid)
    context = {'piano': piano}
    return render(request, "pianos/details.html", context)


def index(request):
    all_pianos = Pianos.objects.using("pianos").all()
    context = {'all_pianos': all_pianos}
    return render(request, "pianos/index.html", context)
