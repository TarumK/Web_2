from django.contrib import admin
from .models import *

# Register your models here.
admin.autodiscover()
admin.site.register(Person)
admin.site.register(Company)