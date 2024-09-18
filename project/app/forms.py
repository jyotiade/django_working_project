

from django import forms
from .models import AdminModel

class AdminRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=100, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password"
    )
    class Meta:
        model = AdminModel
        fields = ('admin_name', 'admin_email', 'admin_city', 'admin_mobile', 'admin_password')
        widgets = {
            'admin_name': forms.TextInput(attrs={'class': 'form-control'}),
            'admin_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'admin_city': forms.TextInput(attrs={'class': 'form-control'}),
            'admin_mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'admin_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = AdminModel
        fields = ('admin_email','admin_password')
        widgets = {
            'admin_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'admin_password':forms.PasswordInput(attrs={'class': 'form-control'}),
        }

