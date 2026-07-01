from django.http import HttpResponse


def home(request):
    return HttpResponse("Clinic Patient Records System - Doctors Module")
