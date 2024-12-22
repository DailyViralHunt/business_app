from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Contact, Appointment, FinancialMatter, LogisticsLead, UploadedFile
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        Contact.objects.create(name=name, phone=phone, email=email)
        return JsonResponse({"message": "Contact added successfully"})

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        UploadedFile.objects.create(file=request.FILES['file'])
        return JsonResponse({"message": "File uploaded successfully"})
    return JsonResponse({"error": "No file uploaded"})

def get_contacts(request):
    contacts = list(Contact.objects.values())
    return JsonResponse({"contacts": contacts})

# Similar views can be created for Appointments, Financial Matters, and Logistics Leads.
