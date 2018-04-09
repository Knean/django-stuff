from django.db import models

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
	