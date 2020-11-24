from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from .forms import AttendeeRegistrationForm, ConferenceCheckoutForm
from .models import Attendee, Conference, Session, Materials, Purchased_Conference
from datetime import date, datetime
from decimal import Decimal
# Create your views here.


def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if Attendee.objects.filter(user=user).exists():
            login(request, user)
            return redirect(home)
        else:
            messages.error(
                request, 'The registered user needs to be a registered attendee!')

    return render(request, template_name='conferences/login.html', context={'form': form})


def register(request):
    form = AttendeeRegistrationForm()
    if request.method == "POST":
        form = AttendeeRegistrationForm(data=request.POST)
        if form.is_valid():
            # User data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Attendee data
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            company_institution = form.cleaned_data['company_institution']
            title = form.cleaned_data['title']
            is_student = form.cleaned_data['is_student']
            try:
                user = User.objects.create(
                    username=username, email=email, first_name=first_name, last_name=last_name)
                user.set_password(raw_password=password)
                user.save()
                user.refresh_from_db()

                attendee = Attendee.objects.create(user=user, address=address, phone=phone,
                                               company_institution=company_institution, title=title, is_student=is_student)
                attendee.save()
                login(request, user)
                return redirect(confirm_registration)
            except IntegrityError as e:
                messages.error(request, 'Error: ' + e)
            
    return render(request, template_name='conferences/register.html', context={'form': form})

def confirm_registration(request):
    return render(request, template_name='conferences/registration_confirmation.html', context={'username': request.user.username})

@login_required
def home(request):
    # Redirect to login page if the user is not an attendee
    if not Attendee.objects.filter(user=request.user).exists():
        print("attendee doesn't exist with that user")
        return redirect(login_request)
    print("home successfully loaded")
    context = {'username': request.user.username}
    return render(request, template_name="conferences/home.html", context=context)


def logout_request(request):
    logout(request)
    return redirect(login_request)


def browse_conferences(request):
    conference_list = Conference.objects.all()
    return render(request, template_name='conferences/browse_conferences.html', context={'conference_list': conference_list})

def conference_detail(request, pk):
    conference = get_object_or_404(Conference, pk=pk) 
    discount_percent = int(conference.discount * 100)
    all_technical_sessions = Session.objects.filter(
        session_type=Session.TECHNICAL)
    technical_session = all_technical_sessions.get(conference=conference)
    all_banquet_tickets = Materials.objects.filter(
        material_type=Materials.BANQUET_TICKETS)
    banquet_ticket = all_banquet_tickets.get(conference=conference)
    original_price = technical_session.cost + banquet_ticket.cost
    original_price = round(original_price,2)
    discount_price = get_discount_price(conference, request.user.attendee, original_price)
    if request.POST.get('confirm_checkout'):
        return redirect(conference_checkout, pk=conference.pk, current_price=str(original_price))
    context = {'conference': conference,'original_price': original_price, 'discount_percent': discount_percent, 'discount_price':discount_price}
    return render(request, template_name='conferences/conference_detail.html',  context=context)

def get_discount_price(conference, attendee, original_price):
    discount = 0
    #Calculate discounts. Students get a 5% discount
    if date.today() <= conference.discount_deadline:
        discount = conference.discount
    if attendee.is_student:
        discount += Decimal(.05) 
    discount_price = original_price * (1 - discount)
    discount_price = round(discount_price, 2)
    return discount_price

def conference_checkout(request, pk, current_price):
    conference = Conference.objects.get(pk=pk)
    current_price = Decimal(current_price)  
    tutorial_session = Session.objects.filter(session_type=Session.TUTORIAL).get(conference=conference)
    workshop_session = Session.objects.filter(session_type=Session.WORKSHOP).get(conference=conference)
    proceedings = Materials.objects.filter(material_type=Materials.PROCEEDINGS).get(conference=conference)
    banquet_tickets = Materials.objects.filter(material_type=Materials.BANQUET_TICKETS).get(conference=conference)
    #Update the form
    form = ConferenceCheckoutForm()
    form.fields['is_tutorial_selected'].label_suffix = " for $" + str(tutorial_session.cost)
    form.fields['is_workshop_selected'].label_suffix = " for $" + str(workshop_session.cost)
    form.fields['proceedings_amt'].label_suffix = ' ($' + str(proceedings.cost) + ' ea.)'
    form.fields['banquet_tickets_amt'].label_suffix = ' ($' + str(banquet_tickets.cost) + ' ea.)'
    
    if request.POST.get('confirm_checkout'):
        print("Confirm button has been pressed.")
        form = ConferenceCheckoutForm(data=request.POST)
        if form.is_valid():
            purchased_conference, created = Purchased_Conference.objects.get_or_create(attendee=request.user.attendee, conference=conference)
            if created:
                print("Purchase created")
            else:
                print("Purchase already exists")
            purchased_conference.proceedings_amt = form.cleaned_data['proceedings_amt']
            purchased_conference.banquet_tickets_amt = form.cleaned_data['banquet_tickets_amt']
            purchased_conference.is_tutorial_purchased = form.cleaned_data['is_tutorial_selected']
            purchased_conference.is_workshop_purchased = form.cleaned_data['is_workshop_selected']
            purchased_conference.payment_type = form.cleaned_data['payment_type']
            purchased_conference.transaction_date_time = datetime.now()
            print("Transaction time = " + purchased_conference.transaction_date_time.strftime('%Y-%m-%d %H:%M'))
            purchased_conference.save()
            
            if purchased_conference.is_tutorial_purchased:
                current_price += tutorial_session.cost
            if purchased_conference.is_workshop_purchased:
                current_price += workshop_session.cost
            current_price += (proceedings.cost * purchased_conference.proceedings_amt) + (banquet_tickets.cost * purchased_conference.banquet_tickets_amt)
            print("Purchased Data Saved")
            current_price = get_discount_price(conference, request.user.attendee, current_price)
            return redirect(checkout_confirmation, pk=conference.pk, price=str(current_price))
    current_price = get_discount_price(conference, request.user.attendee, current_price)
    return render(request, template_name='conferences/conference_checkout.html', context={'conference':conference, 'form':form, 'current_price':current_price})

def checkout_confirmation(request, pk, price):
    conference = Conference.objects.get(pk=pk)
    return render(request, template_name='conferences/checkout_confirmation.html', context={'conference': conference, 'price': price})

class Purchase_Info():
    purchased_conference = None
    technical_session_cost = 0
    tutorial_session_cost = 0
    workshop_session_cost = 0
    proceedings_amt = 0
    proceedings_cost = 0
    banquet_tickets_amt = 1
    banquet_tickets_cost = 0
    student_discount = 0
    conference_discount = 0
    discount_percent = 0
    total = 0
    discount_price = 0
    purchased_date_time = None
    payment_type = None

    def __init__(self, purchased_conference):
        #Collect necessary data from database
        self.purchased_conference = purchased_conference
        conference = purchased_conference.conference
        sessions = Session.objects.filter(conference=conference)
        materials = Materials.objects.filter(conference=conference)
        proceedings = materials.get(material_type=Materials.PROCEEDINGS)
        banquet_tickets = materials.get(material_type=Materials.BANQUET_TICKETS)
        #Populate the fields
        self.technical_session_cost = sessions.get(session_type=Session.TECHNICAL).cost

        if purchased_conference.is_tutorial_purchased:
            self.tutorial_session_cost = sessions.get(session_type=Session.TUTORIAL).cost
        if purchased_conference.is_workshop_purchased:
            self.workshop_session_cost = sessions.get(session_type=Session.WORKSHOP).cost

        self.proceedings_amt = purchased_conference.proceedings_amt
        self.proceedings_cost = proceedings.cost * self.proceedings_amt
        self.banquet_tickets_amt += purchased_conference.banquet_tickets_amt
        self.banquet_tickets_cost = banquet_tickets.cost * self.banquet_tickets_amt

        if purchased_conference.attendee.is_student:
            self.student_discount = Decimal(.05)
        if purchased_conference.transaction_date_time.date() <= conference.discount_deadline:
            self.conference_discount = conference.discount

        self.discount_percent = int((self.student_discount + self.conference_discount) * 100)
        self.total = self.technical_session_cost + self.tutorial_session_cost + self.workshop_session_cost + self.proceedings_cost + self.banquet_tickets_cost
        self.discount_price = get_discount_price(conference, purchased_conference.attendee, self.total)
        self.purchased_date_time = purchased_conference.transaction_date_time
        self.payment_type = purchased_conference.payment_type
        
def view_bill(request):
    all_purchases = Purchased_Conference.objects.filter(attendee=request.user.attendee)
    purchase_info_list = []
    grand_total = 0
    for purchase in all_purchases:
        purchase_info = Purchase_Info(purchase)
        purchase_info_list.append(purchase_info)
        grand_total += purchase_info.discount_price
    context = {'purchase_info_list': purchase_info_list, 'grand_total': grand_total}
    return render(request, template_name='conferences/view_bill.html', context=context)

def remove_purchase(request, pk):
    print("on remove page")
    purchased_conference = Purchased_Conference.objects.get(pk=pk)
    purchase_name = purchased_conference.conference.name
    if request.POST.get('no'):
        print('No was pressed')
        return redirect(view_bill)
    if request.POST.get('yes'):    
        purchased_conference.delete()
        return redirect(remove_purchase_confirmation, purchase_name=purchase_name)
    return render(request, template_name='conferences/remove_purchase.html', context={'purchase_name':purchase_name})

def remove_purchase_confirmation(request, purchase_name):
    return render(request, template_name='conferences/remove_purchase_confirmation.html', context={'purchase_name': purchase_name})
    

