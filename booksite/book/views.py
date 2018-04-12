from django.shortcuts import render
from django.http import HttpResponse
from .models import Chapter
from django.template import Template
from django.template.loader import get_template
from django.http import Http404
# Create your views here.
def home(request):
	template=get_template('book/index.html')
	chapter_list=Chapter.objects.all()
	
	return HttpResponse(template.render({'chapter_list':chapter_list}))
	

def detailchapter(request, chapter_id):
	try:
		chapter_story= Chapter.objects.get(id=chapter_id).chapter_text
	except Chapter.DoesNotExist:
		raise Http404('no such book')
	return HttpResponse('its a chapter numbered: '+str(chapter_id)+'and it goes like this:<br> '+str(chapter_story))
