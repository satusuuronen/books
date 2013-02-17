from django.http import HttpResponse
from django.template import Context, loader
from books_app.models import *
from django.shortcuts import render_to_response

def index(request):
    sort_by = request.GET.get('sort', 'author')
    items_ratm = Item.objects.filter(status=Item.READING).order_by(sort_by, 'author')
    items_tbr = Item.objects.filter(status=Item.TO_BE_READ).order_by(sort_by, 'author')
    items_read = Item.objects.filter(status=Item.READ).order_by(sort_by, 'author')
    items_lib = Item.objects.filter(in_my_library=Item.YES).order_by(sort_by, 'author')
    t = loader.get_template('books_app/to_be_read.html')
    items_ratm = reorganize_blanks(items_ratm, sort_by)
    items_tbr = reorganize_blanks(items_tbr, sort_by)
    items_read = reorganize_blanks(items_read, sort_by)
    items_lib = reorganize_blanks(items_lib, sort_by)
    get_long_book_types(items_ratm)
    get_long_book_types(items_tbr)
    get_long_book_types(items_read)
    get_long_book_types(items_lib)
    c = Context({
        'items_tbr': items_tbr,
        'items_read': items_read,
        'items_ratm': items_ratm,
        'items_lib': items_lib
    })
    return HttpResponse(t.render(c))

def get_long_book_types(list):
    dictionary = dict(Item.BOOK_TYPE_CHOICES)
    for item in list:
        if item.book_type in dictionary:
            item.book_type = dictionary[item.book_type]


def reorganize_blanks(original_listing, sorter):
    listing = list(original_listing)
    if sorter == 'title':
        to_be_moved = []
        for i in range(len(listing)):
            if listing[i].title == '':
                to_be_moved.append(listing[i])
        for item in to_be_moved:
            listing.remove(item)
            listing.append(item)
        return listing
    elif sorter == 'in_my_library':
        to_be_moved = []
        for i in range(len(listing)):
            if listing[i].in_my_library == Item.NO:
                to_be_moved.append(listing[i])
        for item in to_be_moved:
            listing.remove(item)
            listing.append(item)
        return listing
    
    elif sorter == 'book_type':
        dictionary = dict(Item.BOOK_TYPE_CHOICES)
        to_be_moved = []
        for i in range(len(listing)):
            if not listing[i].book_type in dictionary:
                to_be_moved.append(listing[i])
        for item in to_be_moved:
            listing.remove(item)
            listing.append(item)
        return listing 
    elif sorter == 'date_read':
        to_be_moved = []
        for i in range(len(listing)):
            if listing[i].date_read == None:
                to_be_moved.append(listing[i])
        for item in to_be_moved:
            listing.remove(item)
            listing.append(item)
        return listing 

    else: # sorter == 'author':
        return listing
 





            
        



