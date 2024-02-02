from django.contrib import admin
from .models import Image, Service, Trainer
# Register your models here.


admin.site.register(Service)
admin.site.register(Image)
admin.site.register(Trainer)
