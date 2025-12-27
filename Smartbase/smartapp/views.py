import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Application
from .utils import generate_tracking_id
from django.shortcuts import render

def base(request):
        return render(request,'index.html')




def submit_application(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        entrance_exam = request.POST.get('entrance_exam')   # Use the exact field name
        score = request.POST.get('score')
        institution = request.POST.get('institution')      # Use the exact field name
        branch = request.POST.get('branch')

        # Generate unique tracking ID
        tracking_id = generate_tracking_id()
        while Application.objects.filter(application_id=tracking_id).exists():
            tracking_id = generate_tracking_id()

        # Create the Application using correct field names
        app = Application.objects.create(
            application_id=tracking_id,
            full_name=full_name,
            email=email,
            entrance_exam=entrance_exam,
            score=score,
            institution=institution,
            branch=branch
        )

        # Show success page
        return render(request, 'application_success.html', {'tracking_id': app.application_id})

    # Handle GET request → show the form
    return render(request, 'applications.html')

def track_status(request):
     return render(request,'index.html')

def test(request):
     return render(request, "test.html")