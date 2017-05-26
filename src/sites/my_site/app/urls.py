from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^pastors$', views.pastors, name='pastors'),
    url(r'^location$', views.location, name='location'),
    url(r'^calendar$', views.calendar, name='calendar'),
    url(r'^ministries$', views.ministries, name='ministries'),
    url(r'^biblestudies$', views.biblestudies, name='biblestudies'),
    url(r'^sermons$', views.sermons, name='sermons'),
    url(r'^bible_study_schedule', views.bibleStudySchedule, name='bibleStudySchedule'),
    url(r'^women$', views.women, name='women'),
    url(r'^youth$', views.youth, name='youth'),
    url(r'^resources$', views.resources, name='resources'),
    url(r'^pictures$', views.pictures, name='pictures'),
]
