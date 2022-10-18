from django.contrib import admin

from .models import Rating, Article

admin.site.register([Rating, Article])
