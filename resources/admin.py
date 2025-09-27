from django.contrib import admin
from .models import Resource, Comment, Rating, Category

admin.site.register(Resource)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Category)
