from django.contrib import admin
from .models import Course # relative import as models and admin are in same module

# Register your models here.
admin.site.register(Course)