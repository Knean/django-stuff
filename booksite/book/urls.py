from .views import (home,detailchapter)
from django.conf.urls import url
from django.urls import path
app_name='book'
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('<int:chapter_id>/',detailchapter.as_view(),name = 'detail_chapter'),

    

]
