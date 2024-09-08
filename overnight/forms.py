from django import forms
from .models import Guest, Intake, Turnaway

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'

class IntakeForm(forms.ModelForm):
    class Meta:
        model = Intake
        fields = '__all__'

class TurnawayForm(forms.ModelForm):
    class Meta:
        model = Turnaway
        fields = '__all__'