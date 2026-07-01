from django.http import HttpResponse


def home(request):
    return HttpResponse("Clinic Patient Records System - Medical Records Module")
