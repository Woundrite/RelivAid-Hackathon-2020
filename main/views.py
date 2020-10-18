from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core import serializers
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.views import View
from django.views.generic import RedirectView

from .forms import LabourForm, PickerForm, MedicalPillsForm, RegisterForm
from .models import LabourModel, PickerModel, MedicalPill
from. utils import token_gen
from django.http import HttpResponse
# Create your views hered.


def home(request):
    return render(request, 'main/home.html')


def test(request):
    MedicalPill1 = MedicalPill.objects.all()
    context = {'mp':MedicalPill1}
    return render(request, 'main/ecomm.html', context)

def camera(request):
    return render(request, 'main/camera.html')
    
def logout_user(request):
    logout(request)
    return redirect('homepage')        

def first_ques(request):
    if request.method == 'POST':
        if request.POST.get('group1') == "yes":
            return redirect('formtest1')
        else:
            return redirect('formtest')
    return render(request, 'main/first_ques.html')
    
def formtest(request):
    current_year = 2020
    if request.method == 'POST':
        name = request.POST.get('name')
        aadnum = request.POST.get('aadnum')           
        bdate = request.POST.get('bdate')
        bdate = int(bdate[-4:])
        age = current_year - bdate
        x = PickerModel(name=name, age=age, preferToStayAnonymous=True, aadharNumber=aadnum)
        x.save()
        return render(request, 'main/users.html')
    else:
        return render(request, 'main/formtest.html')

def formtest1(request):
    current_year = 2020
    if request.method == 'POST':
        name = request.POST.get('name')
        aadnum = request.POST.get('aadnum')           
        bdate = request.POST.get('bdate')
        going = request.POST.get('going')
        staying = request.POST.get('staying')
        bdate = int(bdate[-4:])
        age = current_year - bdate
        x = LabourModel(name=name, age=age,currentLocation=staying, ishelper=0, gotoLocation=going, aadharNumber=aadnum)
        x.save()
        return render(request, 'main/waiting.html')
    else:
        return render(request, 'main/formtest1.html')


def helping_migrants(request):
    return render(request, 'main/formtest.html') 

def donate(request):
    return render(request, 'main/donate.html')

def contact(request):
    return render(request, 'main/contact.html')