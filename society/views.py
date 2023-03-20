from django.shortcuts import render,redirect
from .models import *
import random
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    try:
        ad_obj=Admin.objects.get(email=request.session['admin_email'])
        return render(request,'index.html',{'ad_obj':ad_obj})
    except:
        return render(request,'login.html')
    
def index2(request):
    return render(request,'index2.html')

def register(request):
    if request.method =='GET':
        return render(request,'register.html')
    else:
        try:
            u_raw=Admin.objects.get(email=request.POST['email'])
            return render(request,'register.html',{'msg':'Email Already Exists'})
        except:
            global computer_otp
            computer_otp=random.randint(100000,999999)
            global u_list
            u_list=[request.POST['full_name'],request.POST['email'],request.POST['password'],request.POST['gender'],request.POST['address']]
            subject='GOKULDHAN SOCIETY'
            message=f'Your OTP is :{computer_otp}'
            from_email= settings.EMAIL_HOST_USER
            to_email=[request.POST['email']]
            send_mail(subject,message,from_email,to_email)
            return render(request,'otp.html')

def otp(request):
    if request.method=='GET':
        return render(request, 'otp.html')
    else:
        if computer_otp==int(request.POST['otp']):    
            Admin.objects.create(
                full_name=u_list[0],
                email=u_list[1],
                password=u_list[2],
                gender=u_list[3],
                Address=u_list[4]
            )
            return render(request,'login.html',{'msg':'Register  Successfully!!'})
        else:
            return render(request,'otp.html',{'msg':'WRONG OTP'})
        
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        try:
            my_obj=Admin.objects.get(email=request.POST['email'])
            if request.POST['password']==my_obj.password:
                request.session['admin_email']=request.POST['email']
                return redirect(index)
            else:
                return render(request,'login.html',{'msg':'Password Wrong'})
        except:
            try:
                my_obj=Member.objects.get(email=request.POST['email'])
                if request.POST['password']==my_obj.password:
                    request.session['admin_email']=request.POST['email']
                    return redirect(index2)
                else:
                    return render(request,'login.html',{'msg':'Password Wrong'})
            
            except:
                try:
                    my_obj=Watchman.objects.get(email=request.POST['email'])
                    if request.POST['password']==my_obj.password:
                        request.session['admin_email']=request.POST['email']
                        return redirect(index2)
                    else:
                        return render(request,'login.html',{'msg':'Password Wrong'}) 
                except:
                    return render(request, 'login.html',{'msg':'Password Wrong'})
                               
                        
        
def logout(request):
    del request.session['admin_email']
    return render(request,'login.html')


def add_member(request):
    my_obj=Admin.objects.get(email=request.session['admin_email'])
    if request.method=='GET':
        return render(request,'add_member.html',{'my_obj':my_obj})
    else:
        admin_obj=Admin.objects.get(email=request.session['admin_email'])
        try:
            u_raw=Member.objects.get(email=request.POST['email'])
            return render(request,'add_member.html',{'msg':'Email Already Exists'})
        except:
            global computer_otp
            computer_otp=random.randint(100000,999999)
            global u_list
            u_list=[request.POST['name'],request.POST['email'],request.POST['password'],request.POST['gender'],request.POST['address']]
            subject='GOKULDHAN SOCIETY'
            message=f'Your OTP is :{computer_otp} send otp to {admin_obj.full_name}'
            from_email= settings.EMAIL_HOST_USER
            to_email=[request.POST['email']]
            send_mail(subject,message,from_email,to_email)
            return render(request,'member_otp.html')
        
def member_otp(request):
    if request.method=='GET':
        return render(request,'member_otp.html')
    else:
        if computer_otp==int(request.POST['otp']):    
            Member.objects.create(
                full_name=u_list[0],
                email=u_list[1],
                password=u_list[2],
                gender=u_list[3],
                Address=u_list[4]
            )
            return render(request,'add_member.html',{'msg':'Add Member Done !!!'})

def add_watchman(request):
    my_obj=Admin.objects.get(email=request.session['admin_email'])
    if request.method=='GET':
        return render(request,'add_watchman.html',{'my_obj': my_obj})
    else:
        admin_obj=Admin.objects.get(email=request.session['admin_email'])
        try:
            u_raw=Watchman.objects.get(email=request.POST['email'])
            return render(request,'add_watchman.html',{'msg':'Email Already Exists'})
        except:
            global com_otp
            com_otp=random.randint(100000,999999)
            global u_list
            u_list=[request.POST['name'],request.POST['email'],request.POST['password'],request.POST['shift'],request.POST['address']]
            subject='GOKULDHAN SOCIETY'
            message=f'Your OTP is :{com_otp} send otp to {admin_obj.full_name}'
            from_email= settings.EMAIL_HOST_USER
            to_email=[request.POST['email']]
            send_mail(subject,message,from_email,to_email)
            return render(request,'watchman_otp.html')

def watchman_otp(request):
    if request.method=='GET':
        return render(request,'watchman_otp.html')
    else:
        if com_otp==int(request.POST['otp']):    
            Watchman.objects.create(
                full_name=u_list[0],
                email=u_list[1],
                password=u_list[2],
                shift=u_list[3],
                Address=u_list[4]
            )
            return render(request,'add_watchman.html',{'msg':'Add Watchman Done !!!'})

def event(request):
    try:
        ad_obj=Admin.objects.get(email=request.session['admin_email'])
        my_event=Event.objects.all()
        return render(request,'event.html',{'my_event':my_event,'ad_obj':ad_obj})
    except:
        my_event=Event.objects.all()
        return render(request,'event.html',{'my_event':my_event})
def notice(request):
    try:
        ad_obj=Admin.objects.get(email=request.session['admin_email'])
        my_notice=Notice.objects.all()
        return render(request,'notice.html',{'my_notice':my_notice, 'ad_obj':ad_obj})
    except:
        my_notice=Notice.objects.all()
        return render(request,'notice.html',{'my_notice':my_notice})

def add_notice(request):
    if request.method=='GET':
        return render(request,'add_notice.html')
    else:
        Notice.objects.create(
            subject=request.POST['subject'],
            notice=request.POST['notice'],
            date=request.POST['date'],
            time=request.POST['time']
        )
        return render(request,'add_notice.html',{'msg':'Notice Added !!'})
    