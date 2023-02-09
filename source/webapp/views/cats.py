from random import random

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.db import Database


def cat_stats(request: WSGIRequest):
    if request.method == 'GET':
        context = {
            'name': Database.cats[0]['name'],
            'age': Database.cats[0]['age'],
            'happiness': Database.cats[0]['happiness'],
            'satiety': Database.cats[0]['satiety'],
            'image': Database.cats[0]['image']
        }
        return render(request, 'cat_stats.html', context)
    match request.POST.get('action'):
        case 'play':
            if Database.cats[0]['state'] == 'sleep':
                Database.cats[0]['happiness'] -= 5
            else:
                if random() < 1 / 3:
                    Database.cats[0]['happiness'] = 0
                else:
                    Database.cats[0]['happiness'] += 15
                    Database.cats[0]['satiety'] -= 10
            Database.cats[0]['state'] = 'play'
        case 'eat':
            Database.cats[0]['happiness'] += 5
            Database.cats[0]['satiety'] += 15
            Database.cats[0]['state'] = 'eat'
        case 'sleep':
            Database.cats[0]['happiness'] += 15
            Database.cats[0]['state'] = 'sleep'
    match Database.cats[0]['state']:
        case 'sleep':
            Database.cats[0]['image'] = '/media/sleep.gif'
        case 'eat':
            Database.cats[0]['image'] = '/media/eat.gif'
            if Database.cats[0]['satiety'] > 100:
                Database.cats[0]['happiness'] -= 30
                Database.cats[0]['image'] = '/media/sad.gif'
        case 'play':
            Database.cats[0]['image'] = '/media/play.gif'
            if Database.cats[0]['happiness'] <= 0:
                Database.cats[0]['image'] = '/media/angry.gif'
    if Database.cats[0]['happiness'] < 0:
        Database.cats[0]['happiness'] = 0
    elif Database.cats[0]['satiety'] < 0:
        Database.cats[0]['satiety'] = 0
    elif Database.cats[0]['happiness'] > 100:
        Database.cats[0]['happiness'] = 100
        Database.cats[0]['image'] = '/media/happy.jpeg'
    context = {
        'name': Database.cats[0]['name'],
        'age': Database.cats[0]['age'],
        'happiness': Database.cats[0]['happiness'],
        'satiety': Database.cats[0]['satiety'],
        'image': Database.cats[0]['image'],
        'state': Database.cats[0]['state']
    }
    return render(request, 'cat_stats.html', context)
