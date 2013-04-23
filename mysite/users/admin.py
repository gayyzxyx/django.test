__author__ = 'gayyzxyx'
from django.contrib import admin
from users.models import Publisher,Author,Book
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)