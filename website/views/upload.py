from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from website.models import User, Mathlete, Waiver

@login_required
def upload(request):
    user_m = request.user
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        waiver = Waiver(
            waiver = uploaded_file,
            user = user_m
        )
        waiver.save()
        
    return render(request, 'upload.html', context)