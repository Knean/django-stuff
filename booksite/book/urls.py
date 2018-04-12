from . import views
from django.conf.urls import url
from django.urls import path
app_name='book'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:chapter_id>/',views.detailchapter,name = 'detail_chapter'),

    

]
