from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def Profile(request):
    return render(request,'profile.html')