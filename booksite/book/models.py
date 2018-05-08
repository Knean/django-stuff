from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
def validate_unique(self, theanswer):
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
	answers=models.ManyToManyField(Answer,validators=[validate_unique])

