from django.contrib import admin
from .models import Articles, Vote, Choice

# Register your models here.

admin.site.register(Articles)
admin.site.register(Vote)
admin.site.register(Choice)