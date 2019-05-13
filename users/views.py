# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate

from django.shortcuts import redirect, render


#class SignUp(generic.CreateView):
#    form_class = CustomUserCreationForm
#    success_url = reverse_lazy('login')
#    template_name = 'signup.html'

def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

#def SignUp(request):
#    if request.method=='POST':
#        form = CustomUserCreationForm(request.POST)
#        if form.is_valid():
#            form.save
#            return redirect('/users')
#    else:
#        form = CustomUserCreationForm()

#        args = {'form': form}
#        return render(request, 'users/signup.html', args)