from django import forms

from realtors.models import User, Realtor


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = "__all__"


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'is_realtor', 'photo']


class UpdateRealtor(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = "__all__"
