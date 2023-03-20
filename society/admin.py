from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Admin)
admin.site.register(Member)
admin.site.register(Watchman)
admin.site.register(Event)
admin.site.register(Notice)