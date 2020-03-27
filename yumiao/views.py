from django.shortcuts import render
from .models import user,cat,admin,application
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def index(request):
    return render(request, 'yumiao/index.html')

def about(request):
    return render(request, 'yumiao/about.html')

def apply(request):
    return render(request, 'yumiao/apply.html')

def gallery(request):
    return render(request, 'yumiao/gallery.html')

def contact(request):
    return render(request, 'yumiao/contact.html')

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

def model(request):
    return render(request, 'yumiao/model.html')

def model_apply(request):
    if request.method == 'GET':
        return render(request, 'yumiao/model_apply.html')
    if request.method == 'POST':
        aname = request.POST.get('appname')
        aage = request.POST.get('appage')
        agender = request.POST.get('appgender')
        aemail = request.POST.get('appemail')
        alocation = request.POST.get('applocation')
        aincome = request.POST.get('appincome')
        areason = request.POST.get('appreason')
        application.appObj.create(appname=aname,appage=aage,appgender=agender,appemail=aemail,applocation=alocation,appincome=aincome,appreason=areason).save()
        return JsonResponse({'success': '200', 'msg': 'Apply successfully!'})

def model_details(request):
    if request.method == 'GET':
        return render(request, 'yumiao/model_details.html')
    if request.method == 'POST':
        cname = request.POST.get('catname')
        cage = request.POST.get('catage')
        cbreed = request.POST.get('catbreed')
        clocation = request.POST.get('catlocation')
        cintroduction = request.POST.get('catintroduction')
        cat.catObj.create(catname=cname, catage=cage, catbreed=cbreed, catlocation=clocation, catintroduction=cintroduction).save()
        return JsonResponse({'success': '200', 'msg': 'Add successfully!'})

def model_change(request):
    if request.method == 'GET':
        return render(request, 'yumiao/model_change.html')
    if request.method == 'POST':
        uname = request.POST.get('username')
        upwd = request.POST.get('userpassword')
        reupwd = request.POST.get('userrepassword')
        print(uname)
        if uname and upwd and reupwd:
            if upwd == reupwd:
                user.userObj.filter(username=uname).update(userpassword=upwd)
                return JsonResponse({'success': '200', 'msg': 'Change successfully!'})
            else:
                return JsonResponse({'success': '202', 'msg': 'Entered passwords differ!'})
        else:
            return JsonResponse({'success': '203', 'msg': 'Can not be empty!'})



