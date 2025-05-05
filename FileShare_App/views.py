from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadFile


def home(request):
    files = UploadFile.objects.all().order_by('-id') 
    return render(request, 'FileShare_App/home.html', {'files': files})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'FileShare_App/upload.html', {'form': form})


def upload_success(request):
    return render(request, 'FileShare_App/success.html')