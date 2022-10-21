from django.contrib import admin
from .models import User, Friends, Lessons

admin.site.register(User)
admin.site.register(Friends)
admin.site.register(Lessons)