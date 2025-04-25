from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def royal1(self):
    return HttpResponse("Hello Everyone")



def home(request):
    # mypage = loader.get_template('firstData.html')
    # return HttpResponse(mypage.render())
    return render(request, 'firstData.html')


def about(request):
    return render(request, 'About.html')