from django import forms
from django.contrib.auth.models import User
from .models import Attendee, Purchased_Conference, Session


""" class AttendeeRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        max_length=100, widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=20)
    company_institution = forms.CharField(
        label='Company/Institution', max_length=200)
    title = forms.CharField(max_length=200)
    is_student = forms.BooleanField(label='Are you a student?', required=False)
    def clean(self):
        cleaned_data = super(AttendeeRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords need to match")

        return cleaned_data """


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name'}

    def clean(self):
        cleaned_data = super().clean()
        check_confirm_password(self, cleaned_data)
        return cleaned_data


def check_confirm_password(instance, cleaned_data):
    password = cleaned_data.get("password")
    confirm_password = cleaned_data.get("confirm_password")

    if password != confirm_password:
        instance.add_error('confirm_password', "Passwords need to match")


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name'}


class AttendeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Attendee
        exclude = ['user']
        labels = {'company_institution': 'Company/Institution',
                  'is_student': 'Are you a student?'}


class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        max_length=100, widget=forms.PasswordInput)
        
    def clean(self):
        cleaned_data = super().clean()
        check_confirm_password(self, cleaned_data)
        return cleaned_data

class ConferenceCheckoutForm(forms.Form):
    is_tutorial_selected = forms.BooleanField(
        required=False, initial=False, label="Add Tutorial Session")
    is_workshop_selected = forms.BooleanField(
        required=False, initial=False, label="Add Workshop Session")
    proceedings_amt = forms.IntegerField(
        min_value=0, required=False, initial=0, label="Add Proceedings")
    banquet_tickets_amt = forms.IntegerField(
        min_value=0, required=False, initial=0, label="Add Additional Banquet Tickets")
    payment_type = forms.ChoiceField(
        required=False, choices=Purchased_Conference.PAYMENT_TYPES, label="Payment Type (on-site)")
