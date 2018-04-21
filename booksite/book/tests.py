from django.test import TestCase
from .models import Answer, Chapter
from django.utils import timezone
# Create your tests here.
class some_silly_test(TestCase):
    def test_this_is_a_retarded_test(self):
        print(Chapter.objects.all())
        mario=Chapter.objects.create(chapter_text="lalala",create_date=timezone.now())
        print(mario.chapter_text)
        self.assertIs(mario.id==2,True)
