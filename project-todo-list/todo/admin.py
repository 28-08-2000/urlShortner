from django.contrib import admin
from .models import Todo

# registering my models
admin.site.register(Todo)