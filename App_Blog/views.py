from django.shortcuts import render

from django.views.generic import CreateView,UpdateView,DeleteView,View,TemplateView,ListView,DetailView

# Create your views here.

def blog_list(request):
    
    return render(request,"App_Blog/blog_list.html",context={})

