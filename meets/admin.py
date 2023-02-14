from django.contrib import admin

# Register your models here.
from meets.models import Meet as Meeting

admin.site.register(Meeting)