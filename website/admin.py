from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Video)
admin.site.register(Showreel)
admin.site.register(Message)
admin.site.register(Reservation)