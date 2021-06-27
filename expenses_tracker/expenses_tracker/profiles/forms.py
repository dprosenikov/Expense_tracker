from django import forms

from expenses_tracker.profiles.models import ProfileModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'