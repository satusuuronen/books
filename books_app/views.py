from django.http import HttpResponse
from django.template import Context, loader
from books_app.models import *
from django.shortcuts import render_to_response

def index(request):
    items_tbr = Item.objects.filter(status=Item.TO_BE_READ).order_by("author")
    items_read = Item.objects.filter(status=Item.READ).order_by("author")
    t = loader.get_template('books_app/to_be_read.html')
    c = Context({
        'items_tbr': items_tbr,
        'items_read': items_read
    })
    return HttpResponse(t.render(c))


