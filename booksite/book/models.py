from django.db import models
from django.conf import settings

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
	chapter=models.OneToOneField(Chapter,on_delete=models.CASCADE)
	answer_text=models.TextField()
	answer_image = models.FileField(upload_to='uploads/')
	def __str__(self):
		return self.answer_text
	
    		

class UserProfile(models.Model):
	player=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	answers=models.ManyToManyField(Answer)
	
def validate_only_one_answer(value):
	for answer in players.answers.all:
		if answer.chapter