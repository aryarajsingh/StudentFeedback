from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ShowTableData/', views.ShowTableData, name='ShowTableData'),
    path('studentfeedback/', views.studentfeedback, name='studentfeedback'),
]