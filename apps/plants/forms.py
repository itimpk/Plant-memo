from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Plant,Group
from django.utils import timezone


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name','variety','plant_date','image','group']
        widgets = {
            'plant_date': forms.DateInput(attrs={'type': 'date','value': timezone.now().strftime('%Y-%m-%d')}),  # adds date picker
        }

    def __init__(self, *args, **kwargs):
        # PULL 'user' from kwargs here:
        user = kwargs.pop('user', None)
        
        super().__init__(*args, **kwargs)
        
        self.fields['group'].empty_label = "Select a group..."
        self.fields['image'].required = False
        
        # Only filter if a user was actually passed
        if user:
            self.fields['group'].queryset = Group.objects.filter(user=user)
        