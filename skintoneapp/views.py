from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import *

# Create your views here.

def Home(request):
    return render(request, 'index.html')


def upload(request):
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')   
    else:
        form = UploadForm()  
    uploads = UserImageDb.objects.all()          
    return render(request, 'upload.html', {'form' : form, 'uploads' : uploads})


def success(request):
    return HttpResponse('Successfully Uploaded')    