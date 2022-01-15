from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from mails.models import *

from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')


def register(request):
    reg=False
    if request.method=="POST":
        user_form=UserFrom(data=request.POST)
        profile_form=ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            return redirect('user_login')
        else:
            return HttpResponse("Invalid Form")
    else:
        user_form=UserFrom()
        profile_form=ProfileForm()
    return render(request,'register.html',{'user_form':user_form,'profile_form':profile_form})



def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"YOUR PASSWORD SUCCESSFULLY UPDATED")
            return render(request,'change_password.html')
        else:
            messages.error(request,"PLEASE CORRECT ERROR")
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'change_password.html',{"form":form})



def update_profile(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        
        update_profile_form=UpdateProfileForm(request.POST,instance=request.user)
        #print(request.user.register)
        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_profile_form=UpdateProfileForm(instance=request.user)
    context={
        'update_form':update_form,
        'update_profile_form':update_profile_form
    }
    return render(request,'update_profile.html',context)




def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        

        if user:
            if user.is_active:
                
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
                       
            else:
                return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid username or password")
    else:
        
        return render(request,'login.html')






def dashboard(request):
    try:
        received=Mail.objects.filter(receiver=request.user.register,trash=False)
        return render(request,'dashboard.html',{'received':received})
    except:
        return render(request,'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')



def add_event(request):
    if request.method=="POST":
        event_form=EventForm(request.POST)
        if event_form.is_valid():
            cp=Event(user=request.user,event_name=event_form.cleaned_data['event_name'],event_date=event_form.cleaned_data['event_date'],event_area=event_form.cleaned_data['event_area'],event_time=event_form.cleaned_data['event_time'],description=event_form.cleaned_data['description'])
            cp.save()
            return render(request,'add_event.html',{'msg':'successfully added event'})
        else:
            return HttpResponse("Invalid form")
    event_form=EventForm()
    return render(request,'add_event.html',{'form':event_form})


def view_all_events(request):
    my_events=Event.objects.all().order_by('-date')
    return render(request,'my_events.html',{'my_events':my_events})





def add_complaint(request):
    if request.method=="POST":
        event_form=ComplaintForm(request.POST)
        if event_form.is_valid():
            cp=Complaint(user=request.user,complaint=event_form.cleaned_data['complaint'])
            cp.save()
            return render(request,'add_event.html',{'msg':'successfully added event'})
        else:
            return HttpResponse("Invalid form")
    event_form=ComplaintForm()
    return render(request,'add_event.html',{'form':event_form})


def view_all_complaints(request):
    my_events=Complaint.objects.all().order_by('-id')
    return render(request,'my_complaint.html',{'my_events':my_events})


def add_feedback(request):
    if request.method=="POST":
        event_form=FeedbackForm(request.POST)
        if event_form.is_valid():
            cp=Feedback(user=request.user,title=event_form.cleaned_data['title'],feedback=event_form.cleaned_data['feedback'])
            cp.save()
            return render(request,'add_event.html',{'msg':'successfully added event'})
        else:
            return HttpResponse("Invalid form")
    event_form=FeedbackForm()
    return render(request,'add_event.html',{'form':event_form})


def view_all_feedback(request):
    my_events=Feedback.objects.all().order_by('-id')
    return render(request,'my_feedback.html',{'my_events':my_events})