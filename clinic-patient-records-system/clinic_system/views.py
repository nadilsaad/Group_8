from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<h1>Clinic Patient Records System</h1>"
        "<p>Welcome. Available modules: "
        "<a href='/patients/'>Patients</a> | "
        "<a href='/doctors/'>Doctors</a> | "
        "<a href='/appointments/'>Appointments</a> | "
        "<a href='/medicalrecords/'>Medical Records</a> | "
        "<a href='/admin/'>Admin</a></p>"
    )
