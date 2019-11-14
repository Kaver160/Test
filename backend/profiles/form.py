from django import forms

from backend.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    """"Форма добавление сообщения"""

class RemoveUser(forms.Form):
    user = forms.CharField()