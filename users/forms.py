# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


#class CustomUserCreationForm(UserCreationForm):
#    email = forms.EmailField(required=True)

#    class Meta(UserCreationForm):
#        models = User
#        fields = (
#            'username', 
#            'first_name',
#            'last_name',
#            'email',
#            'password1',
#            'password2',
#            )
#    
#    def save(self, commit=True):
#        user = super(CustomUserCreationForm, self).save(commit=False)
#        user.first_name = cleaned_data['first_name']
#        user.last_name = cleaned_data['last_name']
#        user.email = cleaned_data['email']
#
#        if commit:
#            user.save()

#        return user
        



#class CustomUserCreationForm(UserCreationForm):

#    class Meta(UserCreationForm):
#        model = CustomUser
#        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')