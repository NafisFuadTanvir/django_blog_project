from django.urls import path
from .import views

app_name= "App_Login"
urlpatterns=[
    
    path("signup/",views.sign_up,name="signup"),
    path("login/",views.login_form,name="login"), 
    path("logout/",views.log_out, name="logout"),
    path("profile/",views.userProfile, name="profile"),
    path("change_profile/",views.userChange,name="change_profile"),
    path("password/",views.changePassword,name="change_password"),
    path("add-pro-pic/",views.add_profilepic,name="add_pro_pic"),
    path("change-pro=pic",views.change_propic,name="change_pro_pic")
]


