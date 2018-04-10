from django.shortcuts import render
from django.http import HttpResponse
from .models import Chapter
# Create your views here.
def home(request):
	return HttpResponse("this is just the beginning")
def detailchapter(request, chapter_id):
    	chapter_story= Chapter.objects.get(id=chapter_id).chapter_text
    	return HttpResponse('its a chapter numbered: '+str(chapter_id)+'and it goes like this:<br> '+str(chapter_story))
