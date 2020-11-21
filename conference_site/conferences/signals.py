from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Attendee, Conference, Session, Materials

@receiver(post_save, sender=Conference)
def on_conference_creation(sender, instance, created, **kwargs):
    if created:  
        create_conference_session(instance, session_type=Session.TECHNICAL)
        create_conference_session(instance, session_type=Session.TUTORIAL)
        create_conference_session(instance, session_type=Session.WORKSHOP)
        create_conference_materials(instance, Materials.BANQUET_TICKETS)
        create_conference_materials(instance, Materials.PROCEEDINGS)
        
def create_conference_session(conference, session_type):
    title = get_conference_title(conference, session_type)
    session = Session(conference=conference, title=title, session_type=session_type)
    session.save()

def create_conference_materials(conference, material_type):
    materials = Materials(conference=conference, material_type=material_type)
    materials.save()

def get_conference_title(conference, session_type):
    return conference.name + ' ' + session_type + ' Session'