from django.contrib import admin
from .models import Book_User
# Register your models here.

def upper_case_name(obj):
    return ("%s" % (obj.id)).upper()
upper_case_name.short_description = 'id'

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'number', upper_case_name)
    list_filter = ('user',)
    search_fields = ['book']

admin.site.register(Book_User, PostAdmin)