from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import signUpForm,Userprofilechange,profile_picture
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def sign_up(request):
    form= signUpForm()
    registered= False
    
    if request.method=="POST":
        form=signUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True
     
    dict={"form":form,"registered":registered}
    return render(request,"App_Login/sign_up.html",context=dict)       
    
def login_form(request):
    form= AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password= form.cleaned_data.get('password') 
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                
    return render(request,'App_Login/login.html',context={"form":form}) 

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def userProfile(request):
    return render(request,"App_Login/user_profile.html",context={}) 

@login_required
def userChange(request):
    current_user= request.user
    form= Userprofilechange(instance=current_user)
    if request.method=="POST":
        
        form=Userprofilechange(request.POST, instance=current_user)
        
        if form.is_valid():
            form.save()
            form= Userprofilechange(instance=current_user)
            
            
    
    return render(request,'App_Login/profile_change.html',context={"form":form})     

@login_required
@csrf_protect
def changePassword(request):
    current_user= request.user
    form= PasswordChangeForm(current_user)
    changed=False
    if request.method=="POST":
        form= PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed=True
    
    return render(request,"App_Login/change_pass.html",context={"form":form, "changed":changed}) 

@login_required
def add_profilepic(request):
    form= profile_picture()
    if request.method=="POST":
        form=profile_picture(request.POST,request.FILES)
        if form.is_valid():
           user_obj= form.save(commit=False)
           user_obj.user= request.user
           user_obj.save()
           return HttpResponseRedirect(reverse("App_Login:profile"))
    
    
    
    return render(request,"App_Login/profile_pic_up.html",context={"form":form})
           

@login_required 
def change_propic(request):
    form= profile_picture(instance=request.user.user_profile)
    if request.method=="POST":
        form=profile_picture(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("App_Login:profile"))
    return render(request,"App_Login/profile_pic_up.html",context={"form":form})
             