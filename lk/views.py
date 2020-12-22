from django.shortcuts import render
from lk.forms import RegistrationForm

# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/login.html', {})
    else:
        form = RegistrationForm()
        return render(request, 'lk/authReg.html', {'form': form})

def lk(request):
    return render(request, 'lk/lk.html')