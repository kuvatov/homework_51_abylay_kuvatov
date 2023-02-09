from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.db import Database


def add_cat(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'index.html')
    Database.cats[0]['name'] = request.POST.get('name').capitalize()
    return redirect('/cat_stats')
