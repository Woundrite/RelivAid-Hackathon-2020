from django.contrib import admin
from .models import LabourModel, PickerModel, MedicalPill
# Register your models here.

admin.site.register(LabourModel)
admin.site.register(PickerModel)
admin.site.register(MedicalPill)