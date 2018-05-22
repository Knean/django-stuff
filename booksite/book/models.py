from django.db import models
from django.conf import settings

from django.core.exceptions import ValidationError
def validate_uniques(theanswer):
	
	for answer in self.answers:
		if answer.chapter==theanswer.chapter:
			raise ValidationError('only one answer per chapter')


# Create your models here.
class Chapter(models.Model):
	chapter_text=models.TextField()
	chapter_image = models.FileField(upload_to='uploads/')
	create_date = models.DateTimeField('date created')
	def __str__(self):
		return self.chapter_text
		#get active user. profile
		#calcualte where to which chapter each answer leads to
		# based on players previous choices


class Answer(models.Model):
	chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE)
	answer_text=models.TextField()
	answer_image = models.FileField(upload_to='uploads/')
	def __str__(self):
		return self.answer_text
	

class Profile(models.Model):
	user=models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
	answers=models.ManyToManyField(Answer,validators=[])
	def clean(self):
		#raise ValidationError('only one answer per chapter')
		
		'''
		for n in range(0,self.answers.all().count()):	
		
			for b in range(0,self.answers.all().count()):
				if self.answers.all()[n].chapter==self.answers.all()[b].chapter and b !=n:
					print("gaaaaaaaaaaaaaaaaaaaaaaaaaaay")'''
					#raise ValidationError('only one answer per chapter')

class PlayerVariables(models.Model):
    	user=models.OneToOneField(Profile, on_delete=models.CASCADE)    	
    	last_chapter= models.CharField(max_length=100)

	