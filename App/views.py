from django.shortcuts import render

# Create your views here.
# Frontend
def frontend(request):
    return render(request,'frontend.html')

# Backend
def backend(request):
    return render(request,'backend.html')