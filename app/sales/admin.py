from django.contrib import admin
from .models import CSV, Position, Sales

admin.site.register(Position)
admin.site.register(Sales)
admin.site.register(CSV)
