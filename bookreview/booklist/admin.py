from django.contrib import admin

# Register your models here.
from .models import Book, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date']
    fieldsets = [
       (None,       {'fields' : ['title', 'author', 'genre', 'wordcount']}),
       ('Time',     {'fields' : ['publish_date'], 'classes' : ['collapse']}) 
    ]
    inlines = [CommentInline]

admin.site.register(Book, BookAdmin)
# admin.site.register(Comment)