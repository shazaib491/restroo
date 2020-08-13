from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(customers)
admin.site.register(add_to_cart)
admin.site.register(reservation)
admin.site.register(team)