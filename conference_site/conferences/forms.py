from django import forms
from .models import Purchased_Conference, Session


class AttendeeRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=20)
    company_institution = forms.CharField(
        label='Company/Institution', max_length=200)
    title = forms.CharField(max_length=200)
    is_student = forms.BooleanField(label='Are you a student?')


class ConferenceCheckoutForm(forms.Form):
    is_tutorial_selected = forms.BooleanField(required=False, initial=False, label="Add Tutorial Session")
    is_workshop_selected = forms.BooleanField(required=False, initial=False, label="Add Workshop Session")
    proceedings_amt = forms.IntegerField(min_value=0, required=False, initial=0, label="Add Proceedings")
    banquet_tickets_amt = forms.IntegerField(min_value=0, required=False, initial=0, label="Add Additional Banquet Tickets")
    payment_type = forms.ChoiceField(required=False, choices=Purchased_Conference.PAYMENT_TYPES, label="Payment Type (on-site)")
