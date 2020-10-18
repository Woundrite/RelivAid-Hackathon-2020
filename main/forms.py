from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import LabourModel, PickerModel, MedicalPill
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password1',
			'password2',
		]
class LabourForm(forms.ModelForm):
    class Meta:
        model = LabourModel
        fields = "__all__"

class PickerForm(forms.ModelForm):
    class Meta:
        model = PickerModel
        fields = "__all__"
    
class MedicalPillsForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.IntegerField()

    class Meta:
        model = MedicalPill
        fields = ("name", "price", "nameOfStore")