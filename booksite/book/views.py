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
	print(request.body)
	try:
		chapter= Chapter.objects.get(id=chapter_id)
	except Chapter.DoesNotExist:
		raise Http404('no such book')
	if  request.POST:
		print(request.POST)
		chapter.chapter_text = request.POST.get('text')
		#chapter.save() 
	

	return  render(request,'book/detail.html',context= {'chapter':chapter})
	
