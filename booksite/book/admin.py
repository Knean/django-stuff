from django.contrib import admin
from .models import Chapter, Answer, UserProfile
# Register your models here.
admin.site.register(Chapter)
admin.site.register(Answer)
admin.site.register(UserProfile)