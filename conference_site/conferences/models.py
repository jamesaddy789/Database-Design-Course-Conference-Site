from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.urls import reverse
#### Entities ####


class Attendee(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    # Email and Name are included in the User model
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    company_institution = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    is_student = models.BooleanField()

    def __str__(self):
        return self.user.get_full_name()

class Conference(models.Model):
    name = models.CharField(max_length=200, default="Conference")
    description = models.TextField(default="This is a conference.")
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_deadline = models.DateField(default=date.today)

    def __str__(self):
        return self.name

class Conference_Date_Time(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField(default=datetime.now())
    end_date_time = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.conference.name + ' Date/Time'
    class Meta:
        verbose_name = 'Conference Date Time'


class Session(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="Title")
    TECHNICAL = 'Technical'
    TUTORIAL = 'Tutorial'
    WORKSHOP = 'Workshop'
    TYPES = [(WORKSHOP, WORKSHOP), (TUTORIAL, TUTORIAL),
             (TECHNICAL, TECHNICAL)]
    max_string_length = max(len(TECHNICAL), len(TUTORIAL), len(WORKSHOP))
    session_type = models.CharField(
        max_length=max_string_length, choices=TYPES, default=TECHNICAL)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=10)

    def __str__(self):
        return self.title


class Materials(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    BANQUET_TICKETS = 'Banquet Tickets'
    PROCEEDINGS = 'Proceedings'
    TYPES = [(BANQUET_TICKETS, BANQUET_TICKETS), (PROCEEDINGS, PROCEEDINGS)]
    max_string_length = max(len(BANQUET_TICKETS), len(PROCEEDINGS))
    material_type = models.CharField(
        max_length=max_string_length, choices=TYPES, default=BANQUET_TICKETS)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=5)

    class Meta:
        verbose_name_plural = "Materials"

#### Relations ####
class Speaks(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Speaks"

#This relation holds the information for an attendee's purchase of a conference.
#The purchase of a conference automatically includes the technical session and 1 banquet ticket.
class Purchased_Conference(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    proceedings_amt = models.IntegerField(default=0)
    banquet_tickets_amt = models.IntegerField(default=0)
    is_tutorial_purchased = models.BooleanField(default=False)
    is_workshop_purchased = models.BooleanField(default=False)
    CREDIT_CARD = 'Credit Card'
    CASH = 'Cash'
    CHECK = 'Check'
    max_string_length = max(len(CREDIT_CARD), len(CASH), len(CHECK))
    PAYMENT_TYPES = [(CREDIT_CARD, CREDIT_CARD), (CASH, CASH), (CHECK, CHECK)]
    payment_type = models.CharField(max_length=max_string_length, choices=PAYMENT_TYPES, default=CREDIT_CARD)
    transaction_date_time = models.DateTimeField(default=datetime.now())