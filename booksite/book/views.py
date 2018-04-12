from django.shortcuts import render
from django.http import HttpResponse
from .models import Chapter
from django.template import Template
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render
# Create your views here.
def home(request):
	template=get_template('book/index.html')
	chapter_list=Chapter.objects.all()
	
	return HttpResponse(template.render({'chapter_list':chapter_list}))
	

def detailchapter(request, chapter_id):
	try:
		chapter= Chapter.objects.get(id=chapter_id)
	except Chapter.DoesNotExist:
		raise Http404('no such book')
	return  render(request,'book/detail.html',context= {'chapter':chapter})
	
