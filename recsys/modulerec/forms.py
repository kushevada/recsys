from django import forms
from django.contrib.auth.models import User
from moduleauth.models import Profile
from django.core.exceptions import ValidationError


# Create your forms here.
# форма для выбора цели
class GoalForm(forms.Form):
    goal = forms.ChoiceField(
        label='Выберите цель',
        choices=[
            ('gain', 'Набор массы'),
            ('lose', 'Похудение'),
            ('main', 'Поддержание веса')
        ],
        widget=forms.RadioSelect)
    
# class RecFilterForm(forms.Form):
#     filter = forms.ChoiceField(
#         label='Фильтр',
#         choices=[
#             ('excluded', 'Исключенные'),
#             ('allowed', 'Разрешенные'),
#             ('recommended', 'Рекомендованные')
#         ],
#         widget=forms.RadioSelect)