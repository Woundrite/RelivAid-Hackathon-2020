from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('medicine/', views.test, name='medicine'),
    path('camera/', views.camera, name='camera'),
    path('helping_migrants/', views.helping_migrants, name='helping_migrants'),
    path('first_ques/', views.first_ques, name='first_ques'),
    path('formtest/', views.formtest, name='formtest'),
    path('formtest1/', views.formtest1, name='formtest1'),
    path('logout/', views.logout_user, name='logout_user'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
]