from django.shortcuts import render
from .models import services_model

# Create your views here.

def services(request):
    all_services = services_model.objects.all()
    return render(request, 'services.html', {'all_services_key': all_services})