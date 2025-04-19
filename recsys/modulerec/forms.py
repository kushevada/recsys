from django import forms
from .models import Product
from moduleauth.models import Profile


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
    
# форма для отметок продуктов
class ExcludedProductsForm(forms.ModelForm):
    excluded_products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Продукты, которые нельзя употреблять"
    )

    class Meta:
        model = Profile
        fields = ['excluded_products']