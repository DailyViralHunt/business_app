from django.contrib import admin
from .models import Contact, Appointment, FinancialMatter, LogisticsLead, UploadedFile

# Register your models here.

admin.site.register(Contact)
admin.site.register(Appointment)
admin.site.register(FinancialMatter)
admin.site.register(LogisticsLead)
admin.site.register(UploadedFile)
