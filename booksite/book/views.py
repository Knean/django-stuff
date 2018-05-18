from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Chapter
from django.template import Template
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import ChapterForm
from django.contrib.auth import get_user
# Create your views here.
class home(View):
	def get(self, request, *args, **kwargs):
		template=get_template('book/index.html')
		chapter_list=Chapter.objects.all()
		
		return HttpResponse(template.render({'chapter_list':chapter_list}))
class start(FormView):
    	
		form_class= ChapterForm
		print(dir(form_class),'wwwwwwwwwwwtf')
		template_name= 'book/form.html'
		success_url = '/thanks/'
		
		def get_form_kwargs(self):
			initial = super().get_form_kwargs()
			initial['user']=get_user(self.request)
			return initial
		def get_form(self,*args,**kwargs):
			self.form_class.declared_fields['field1'].queryset=kwargs.pop('user',None)
			
			super().get_form()
		#print('viiiiew',print(inital))
    	#def get(self, request, *args, **kwargs):
    			#form = ChapterForm
    			
		

class detailchapter(TemplateView):
	template_name='book/detail.html'

	def get_context_data(self, **kwargs):
		try:
			chapter= Chapter.objects.get(id=kwargs.get('chapter_id'))
		
		except Chapter.DoesNotExist:
			raise Http404('no such book')
		context = super().get_context_data(**kwargs)
		context['chapter'] = chapter
		
		return context
	def get(self, request, *args, **kwargs):
		template_name='book/detail.html'

		print(request.body)

		return super().get(self, request, *args, **kwargs)
		
	def post(self, request, *args, **kwargs):
			chapter= Chapter.objects.get(id=kwargs.get('chapter_id'))
			print(request.POST)
			chapter.chapter_text = request.POST.get('text')
			print(request.POST.get('text'))
			chapter.save() 
			return redirect('book:detail_chapter', chapter_id=kwargs['chapter_id'])
			

		#return  render(request,'book/detail.html',context={'chapter':chapter})
	
