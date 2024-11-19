from django.urls import path
from .import views
app_name= "App_Login"
urlpatterns=[
    
    path("signup/",views.sign_up,name="signup"),
    path("login/",views.login_form,name="login"), 
    path("logout/",views.log_out, name="logout"),
    path("profile/",views.userProfile, name="profile"),
    path("change_profile/",views.userChange,name="change_profile")
]