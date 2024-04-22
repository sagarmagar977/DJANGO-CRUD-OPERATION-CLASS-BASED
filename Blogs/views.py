from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


class postview(ListView):
    model=post
    template_name="home.html"

class postdetail(DetailView):
    model=post
    template_name='detail.html'

class newpost(CreateView):
    model=post
    template_name="new.html"
    fields=['title','author','body']

class updatepost(UpdateView):
    model=post
    template_name='update.html'
    fields=['title','body']

class deletepost(DeleteView):
    model=post
    template_name="delete.html"
    success_url=reverse_lazy("home")




# Create your views here.
