from django.contrib import admin
from .models import * 

admin.site.register(Products)
admin.site.register(record)

admin.site.site_header = 'Social_help'
# Register your models here.
