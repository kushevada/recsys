from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError


# Create your forms here.
class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Пользователь с таким адресом уже зарегестрирован')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.get_or_create(user=user)
        return user
    


class UserInfoForm(forms.ModelForm):
    sex = forms.ChoiceField(label='Пол', required=True, choices=[('male', 'Мужской'), ('female', 'Женский')])
    age = forms.IntegerField(label='Возраст', required=True)
    height = forms.IntegerField(label='Рост', required=True)
    weight = forms.IntegerField(label='Вес', required=True)
    goal = forms.ChoiceField(label='Цель', choices=Profile._meta.get_field('goal').choices, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ('sex', 'age','height', 'weight', 'goal')
        widgets = {
            'sex': forms.RadioSelect(choices=[('male', 'Мужской'), ('female', 'Женский')]), 
            'age': forms.NumberInput(attrs={'min': 0, 'max': 120}), 
            'height': forms.NumberInput(attrs={'min': 120, 'max': 300}), 
            'weight': forms.NumberInput(attrs={'min': 25, 'max': 300})
        }

    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height < 120 or height > 300:
            raise forms.ValidationError('Некорректные данные')
        return height

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight < 25 or weight > 300:
            raise forms.ValidationError('Некорректные данные')
        return weight