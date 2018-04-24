from django.test import TestCase
from .models import Answer, Chapter
from django.utils import timezone
from django.urls import reverse
# Create your tests here.
class some_silly_test(TestCase):
    def test_this_is_a_retarded_test(self):
        
        mario=Chapter.objects.create(chapter_text="lalala",create_date=timezone.now())
       
        self.assertIs(mario.id==1,True)
    def testing_if_client_works(self):
        response = self.client.get(reverse('book:home'))
        print('response: ',response.content, '\n','context',response.context)
        self.assertIs(response==True,True)
