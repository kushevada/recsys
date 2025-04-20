from django import forms
from .models import Rating


# Create your forms here.
class RatingForm(forms.Form):
    value = forms.ChoiceField(
        label='Рейтинг',
        choices=[(i, i) for i in range(1, 6)],  # 1 to 5
        widget=forms.RadioSelect
    )