from django.contrib import admin
from .models import (Contact, DisplayPicture)

# Register your models here.
admin.site.register(model_or_iterable=(Contact, DisplayPicture))
