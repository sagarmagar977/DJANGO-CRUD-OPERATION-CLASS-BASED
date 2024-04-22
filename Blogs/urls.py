from django.urls import path,include
from .views import *

urlpatterns = [
    path("", postview.as_view(),name="home"),
    path("post/<int:pk>/",postdetail.as_view(),name='detail'),
    path("post/new/",newpost.as_view(),name="new"),
    path("post/<int:pk>/update/",updatepost.as_view(),name="updatepost"),
    path("post/<int:pk>/delete/",deletepost.as_view(),name='deletepost')
    
]

