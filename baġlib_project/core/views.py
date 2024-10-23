import os
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.http import HttpResponse
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

from django.http import HttpResponse

def index(request):
    return HttpResponse("React app should load here!")