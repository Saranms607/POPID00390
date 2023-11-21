from django.contrib import admin
from .models import Doctors
from .models import Medicine
# Register your models here.
admin.site.register(Doctors)
admin.site.register(Medicine)