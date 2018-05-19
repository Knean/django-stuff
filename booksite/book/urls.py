from .views import (home,detailchapter,start)
from django.conf.urls import url
from django.urls import path
app_name='book'
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('<int:chapter_id>/',detailchapter.as_view(),name = 'detail_chapter'),
    path('start',start.as_view(),name='start')

    

]
