from django.http import HttpResponse
from django.template import Context, loader
from books_app.models import *
from django.shortcuts import render_to_response

def index(request):
    items_ratm = Item.objects.filter(status=Item.READING).order_by("author")
    items_tbr = Item.objects.filter(status=Item.TO_BE_READ).order_by("author")
    items_read = Item.objects.filter(status=Item.READ).order_by("author")
    t = loader.get_template('books_app/to_be_read.html')
    get_long_book_types(items_ratm)
    get_long_book_types(items_tbr)
    get_long_book_types(items_read)
    c = Context({
        'items_tbr': items_tbr,
        'items_read': items_read,
        'items_ratm': items_ratm
    })
    return HttpResponse(t.render(c))

def get_long_book_types(list):
    dictionary = dict(Item.BOOK_TYPE_CHOICES)
    for item in list:
        if dictionary.has_key(item.book_type):
            item.book_type = dictionary[item.book_type]
        



