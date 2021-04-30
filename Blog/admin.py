from django.contrib import admin
from .models import Article # relative import as models and admin are in same module

# Register your models here.
admin.site.register(Article)
