from django.http import HttpResponse
from django.shortcuts import render
from .models import Royal
from django.template import loader
# Create your views here.


def royal1(self):
    return HttpResponse("Hello Everyone")



# def home(request):
    # mypage = loader.get_template('firstData.html')
    # return HttpResponse(mypage.render())
    # return render(request, 'firstData.html')

# def home(request):
#     allusers = Royal.objects.all().values()
#     mytemp = loader.get_template('user.html')
#     context  = {
#         'allusers' : allusers
#     }
#     return HttpResponse(mytemp.render(context,request))

def home(request):
    allusers = Royal.objects.all().values()
    mytemp = loader.get_template('allusers.html')
    context  = {
        'allusers' : allusers
    }
    return HttpResponse(mytemp.render(context,request))



def linksdetails(request,id):
    user = Royal.objects.get(id=id)
    mtemp1 = loader.get_template('linksdetails.html')
    context = {
        'user' : user
    }
    return HttpResponse(mtemp1.render(context,request))

def about(request):
    return render(request, 'About.html')
