from django.shortcuts import render
from .models import Profile

# Create your views here.
def resume_view(request):
    profile = Profile.objects.first()
    return render(request,'resume_app/resume_app.html',{'profile':profile})