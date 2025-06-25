from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def getData(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers' : mymembers
  }
  return HttpResponse(template.render(context,request))

def django_basic(request):
  template = loader.get_template('django_basic.html')
  context = {
    'xyz' : "django_basic Variable",
    'abc' : "Royal",
    'royal' : 2,
    # 'mydata' : range(10)
    # 'mydata' : [11,12,13,14]
    'mydata' : ["Royal","Tech","soft"]
  }
  return HttpResponse(template.render(context,request))


def loaderpage(request):
  template = loader.get_template('loaderpage.html')
  return HttpResponse(template.render())



def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def portfolio(request):
  template = loader.get_template('portfolio.html')
  return HttpResponse(template.render())