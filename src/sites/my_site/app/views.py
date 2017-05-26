# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

def index(request):
  return render(request, 'app/index.html', {"page":"home"})

def about(request):
  return render(request, 'app/about.html', {"page":"about"})

def pastors(request):
  return render(request, 'app/pastors.html', {"page":"about"})

def location(request):
  return render(request, 'app/location.html', {"page":"about"})

def calendar(request):
  return render(request, 'app/calendar.html', {"page":"about"})

def ministries(request):
  return render(request, 'app/ministries.html', {"page":"ministries"})

def biblestudies(request):
  return render(request, 'app/biblestudies.html', {"page":"ministries"})

def sermons(request):
  return render(request, 'app/sermons.html', {"page":"sermons"})

def bibleStudySchedule(request):
  return render(request, 'app/bible_study_schedule.html', {"page":"ministries"})

def women(request):
  return render(request, 'app/women.html', {"page":"women"})

def youth(request):
  return render(request, 'app/youth.html', {"page":"youth"})

def resources(request):
  return render(request, 'app/resources.html', {"page":"resources"})

def pictures(request):
  return render(request, 'app/pictures.html', {"page":"resources"})

def handler_500(request):
    r = render(request, '500.html')
    r.status_code = 500
    return r

def handler_404(request):
    r = render(request, '404.html')
    r.status_code = 404
    return r