from django.shortcuts import render
from .models import user,cat,admin,application
from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, 'yumiao/index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'yumiao/login.html')
    if request.method == 'POST':
        uname = request.POST.get('username')
        upwd = request.POST.get('userpassword')
        if uname == '':
            return JsonResponse({'success': '203', 'msg': 'Username can not be empty!'})
        else:
            if upwd == '':
                return JsonResponse({'success': '204', 'msg': 'Password can not be empty!'})
            else:
                user_obj = user.userObj.filter(username=uname).first()
                if user_obj:
                    pass_obj = user.userObj.filter(userpassword=upwd).first()
                    if pass_obj:
                        return JsonResponse({'success': '200', 'msg': 'Success', 'username': uname})
                    else:
                        return JsonResponse({'success': '202', 'msg': 'Entered wrong passwords!'})
                else:
                    return JsonResponse({'success': '201', 'msg': 'Username not existed!'})

def register(request):
    if request.method == 'GET':
        return render(request, 'yumiao/register.html')
    if request.method == 'POST':
        uname = request.POST.get('username')
        upwd = request.POST.get('userpassword')
        reupwd = request.POST.get('userrepassword')
        utel = request.POST.get('usertelephone')
        umail = request.POST.get('useremail')
        if uname and upwd and reupwd:
            if upwd == reupwd:
                user_obj = user.userObj.filter(username=uname).first()
                if user_obj:
                    return  JsonResponse({'success': '201', 'msg': 'Username existed!'})
                else:
                    user.userObj.create(username=uname, userpassword=upwd, usertelephone=utel, useremail=umail).save()
                    return JsonResponse({'success': '200', 'msg': 'Register successfully!'})
            else:
                return  JsonResponse({'success': '202', 'msg': 'Entered passwords differ!'})

        else:
            return  JsonResponse({'success': '203', 'msg': 'Can not be empty!'})

def forgot(request):
    return render(request, 'yumiao/forgot.html')
