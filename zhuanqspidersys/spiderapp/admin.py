from django.contrib import admin

# Register your models here.
from spiderapp.models import Work, Author, Style

admin.site.register(Work)
admin.site.register(Author)
admin.site.register(Style)