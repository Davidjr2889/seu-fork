from django import forms
from .models import Model_coin

class Form_Coin(forms.ModelForm):
    class Meta:
        model = Model_coin
        fields = [
            'coin_send',
            'type_send',
            'type_return'
        ]