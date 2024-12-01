from django.urls import path
from .import views

app_name= "App_Blog"

urlpatterns=[
    
    path("",views.BlogList.as_view(),name="blog_list"),
    path("write/",views.Create_Blog.as_view(),name="create_blog"),
    
]