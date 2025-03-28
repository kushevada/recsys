from django import forms
from django.contrib.auth.models import User
from .models import Profile


# Create your forms here.
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(user__iexact=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует.')
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            Profile.objects.get_or_create(user=user)
        return user