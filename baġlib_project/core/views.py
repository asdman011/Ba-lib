from django.shortcuts import render, redirect
from .forms import ProfileForm

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'index.html', {'form': form})
