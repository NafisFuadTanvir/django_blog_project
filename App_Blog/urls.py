from django.urls import path
from .import views

app_name= "App_Blog"

urlpatterns=[
    
    path("",views.BlogList.as_view(),name="blog_list"),
    path("write/",views.Create_Blog.as_view(),name="create_blog"),
    path('details/<slug:slug>', views.blog_details, name='blog_details'),
    path("liked/<pk>/",views.liked,name="blog_liked"),
    path("unliked/<pk>/",views.unliked,name="blog_unliked"),
    path("my-blogs/",views.MyBlogs.as_view(),name="my_blogs"),
    path("edit-blogs/<pk>/",views.UpdateBlog.as_view(),name="edit_blog")
    
]