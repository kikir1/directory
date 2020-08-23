from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('directory/<int:page>', views.DirectoryListView.as_view()),
    path('directory/<int:pk>/<int:page>', views.DirectoryDetailListView.as_view()),
    path('directory/<int:pk>/<str:version>/<int:page>', views.DirectoryVersionDetailListView.as_view()),
    path('directory/<str:date>/<int:page>', views.DirectoryDateListView.as_view()),
    path('directory/create', views.DirectoryCreateView.as_view())
]
