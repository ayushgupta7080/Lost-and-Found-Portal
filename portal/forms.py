# portal/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, LostItem, FoundItem

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    contact = forms.CharField(max_length=15, required=True)
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'contact', 'gender', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                email=self.cleaned_data['email'],
                contact=self.cleaned_data['contact'],
                gender=self.cleaned_data['gender']
            )
        return user

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'email', 'contact', 'gender', 'location', 'profile_pic']

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['title', 'description', 'category', 'location', 'image']

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['title', 'description', 'category', 'location', 'image']
