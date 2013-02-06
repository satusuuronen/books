from django.db import models
from django.contrib import admin


class Item(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    second_title = models.CharField(max_length=200, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_read = models.DateField('date read', blank=True, null=True) 
    description = models.TextField(blank=True)
    TO_BE_READ = 'TBR'
    READ = 'READ'    
    READING = 'RATM'
    STATUS_CHOICES = (
        (TO_BE_READ, 'To-Be-Read'),
        (READ, 'Read'),
        (READING, 'Reading at the Moment'),
    )
    status = models.CharField(max_length=4,choices= STATUS_CHOICES, default=TO_BE_READ)
    FICTION = 'FICTION'
    NON_FICTION = 'NON_FIC'
    CODING = 'CODING'
    BOOK_TYPE_CHOICES = (
        (FICTION, 'Fiction'),
        (NON_FICTION, 'Non-Fiction'),
        (CODING, 'Coding'),
    )
    book_type = models.CharField(max_length=7, choices=BOOK_TYPE_CHOICES, blank=True)

    def __unicode__(self):
        return self.author

class ItemAdmin(admin.ModelAdmin):
    search_fields = ["author"]

admin.site.register(Item, ItemAdmin)


class User(models.Model):
    user_id = models.IntegerField()
    name =  models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField(blank=True)

