from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        form = Waiver(
          waiver =  uploaded_file,
          user = user_m
        )
        form.save()
        fs = FileSystemStorage()
        context['url'] = fs.url(form.waiver.name)

    return render(request, 'upload.html', context)

