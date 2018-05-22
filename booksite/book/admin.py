from django.contrib import admin
from .models import Chapter, Answer,Profile, PlayerVariables
from .forms import ProfileForm
#Register your models here.
admin.site.register(Chapter)
admin.site.register(Answer)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
   
admin.site.register(Profile, ProfileAdmin, )
admin.site.register(PlayerVariables )