from django.contrib import admin
from .models import Appointment, extended_user,Blog

admin.site.register(extended_user)
admin.site.register(Blog)
admin.site.register(Appointment)
# Register your models here.
