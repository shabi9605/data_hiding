from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect



from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def compose_mail(request):
    if request.method=="POST":
        company_form=ComposeMailForm(request.POST,request.FILES)
        if company_form.is_valid():
            cp=Mail(user=request.user,receiver=company_form.cleaned_data['receiver'],subject=company_form.cleaned_data['subject'],
            message=company_form.cleaned_data['message'],image=company_form.cleaned_data['image'],
            key=company_form.cleaned_data['key'])
            
            #print(cp.receiver.user)
            
            #print(cp.receiver.user.email)
            
            send_mail('You have received a message, Thats Secret key is ',str(cp.key),'shabi960580@gmail.com',[cp.receiver.user.email])
            cp.save()
            return render(request,'compose_mail.html',{'msg':'successfully added mail'})
        else:
            return HttpResponse("Invalid form")
    company_form=ComposeMailForm()
    return render(request,'compose_mail.html',{'form':company_form})



def view_send_messages(request):
    sented_items=Mail.objects.filter(user=request.user,trash=False)

    return render(request,'view_sent_mails.html',{'sented_items':sented_items})



def view_particular_mail1(request,id):
    if request.method=="POST":
        key=request.POST.get('key')
        try:
            mail=Mail.objects.get(key=key,id=id)
            return render(request,'view_full_message.html',{'mail':mail})

        except:
            return HttpResponse("Invalid Key")

        
        
        #return HttpResponse("Invalid form")
    company_form=ComposeMailForm()
    return render(request,'view_full_message.html')


def move_trash(request,id):
    mail=Mail.objects.get(id=id)
    mail=Mail.objects.update_or_create(id=id,
    defaults={'trash':True})
    return redirect('view_send_messages')



def view_trash(request):
    trash=Mail.objects.filter(user=request.user,trash=True)
    return render(request,'trash.html',{'trash':trash})
