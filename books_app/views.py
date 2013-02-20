from django.http import HttpResponse
from django.template import Context, loader
from books_app.models import *
from django.shortcuts import render_to_response

def index(request):
    sort_by = request.GET.get('sort', 'author')
    items_ratm = Item.objects.filter(status=Item.READING) 
    items_tbr = Item.objects.filter(status=Item.TO_BE_READ) 
    items_read = Item.objects.filter(status=Item.READ) 
    items_lib = Item.objects.filter(in_my_library=Item.YES)     
    t = loader.get_template('books_app/to_be_read.html')
    items_ratm = list_sorter(items_ratm, sort_by)
    items_tbr = list_sorter(items_tbr, sort_by)
    items_read = list_sorter(items_read, sort_by)
    items_lib = list_sorter(items_lib, sort_by)
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


def list_sorter(original_listing, sorter):
    listing = list(original_listing)
    if sorter == 'title':
        listing.sort(scandinavian_chracter_sort_by_title)
        to_be_moved = []
        for i in range(len(listing)):
            if listing[i].title == '':
                to_be_moved.append(listing[i])
        for item in to_be_moved:
            listing.remove(item)
            listing.append(item)
        return listing
    elif sorter == 'in_my_library':
        listing.sort(scandinavian_chracter_sort_by_in_my_library)
        return listing
    
    elif sorter == 'book_type':
        listing.sort(scandinavian_chracter_sort_by_book_type)
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
        listing.sort(scandinavian_chracter_sort_by_date_read)
        to_be_moved = []
        for i in range(len(listing)):
            if listing[i].date_read == None:
                to_be_moved.append(listing[i])
        for item in to_be_moved:
            listing.remove(item)
            listing.append(item)
        return listing 

    else: # sorter == 'author':
        listing.sort(scandinavian_chracter_sort_by_author)
        return listing

def scandinavian_chracter_sort_by_author(x,y):
    x1 = x.author.lower()
    y1 = y.author.lower()
    length = min(len(x1), len(y1))
    for i in range(length):
        if x1[i] > y1[i]:
            return 1
        if x1[i] < y1[i]:
            return -1
        #if x[i] == 'a'
    if len(x1) > len(y1):
        return 1
    elif len(x1) < len(y1):
        return -1
    return 0
    
def scandinavian_chracter_sort_by_in_my_library(x,y):
    x1 = x.in_my_library
    y1 = y.in_my_library
    if x1 == Item.YES and y1 == Item.NO:
        return 1
    elif x1 == Item.NO and y1 == Item.YES:
        return -1
    return scandinavian_chracter_sort_by_author(x,y)

def scandinavian_chracter_sort_by_date_read(x,y):
    x1 = x.date_read
    y1 = y.date_read
    if x1 == None and y1 == None:
        return scandinavian_chracter_sort_by_author(x,y)
    if x1 == None:
        return -1
    if y1 == None:
        return 1
    if x1 > y1:
        return 1
    if x1 < y1:
        return -1
    return scandinavian_chracter_sort_by_author(x,y)

    
def scandinavian_chracter_sort_by_book_type(x,y):
    x1 = x.book_type.lower()
    y1 = y.book_type.lower()
    length = min(len(x1), len(y1))
    for i in range(length):
        if x1[i] > y1[i]:
            return 1
        if x1[i] < y1[i]:
            return -1
        #if x[i] == 'a'
    if len(x1) > len(y1):
        return 1
    elif len(x1) < len(y1):
        return -1
    return scandinavian_chracter_sort_by_author(x,y)
 
def scandinavian_chracter_sort_by_book_type(x,y):
    x1 = x.book_type.lower()
    y1 = y.book_type.lower()
    length = min(len(x1), len(y1))
    for i in range(length):
        if x1[i] > y1[i]:
            return 1
        if x1[i] < y1[i]:
            return -1
        #if x[i] == 'a'
    if len(x1) > len(y1):
        return 1
    elif len(x1) < len(y1):
        return -1
    return scandinavian_chracter_sort_by_author(x,y)

 





            
        



