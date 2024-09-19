from django import forms
from .models import Guest, Intake, Turnaway

class DateInput(forms.DateInput):
    input_type = 'date'

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'
        widgets = {
            'date': DateInput
        }

class IntakeForm(forms.ModelForm):
    class Meta:
        model = Intake
        fields = '__all__'
        widgets = {
            'date': DateInput
        }

class TurnawayForm(forms.ModelForm):
    class Meta:
        model = Turnaway
        fields = '__all__'