from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from App_login.models import UserProfile,Follow
from django.contrib.auth.models import User


# Create your views here.

@login_required
def home(request):
    following_list=Follow.objects.filter(follower=request.user)
    if request.method == 'GET':
        search = request.GET.get('search',' ')
        result=User.objects.filter(username__contains=search)
    return render(request,'App_Posts/home.html',context={'title':'Home','search':search,'result':result,'following_list':following_list })