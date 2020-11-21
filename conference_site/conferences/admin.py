from django.contrib import admin
from django.contrib.auth.models import User
from .models import Conference, Session, Materials, Conference_Date_Time, Speaks, Attendee, Purchased_Conference

class Session_Inline(admin.StackedInline):
    extra = 0
    max_num = 3
    model = Session

class Material_Inline(admin.StackedInline):
    extra = 0
    max_num = 2
    model = Materials

class Conference_Date_Time_Inline(admin.StackedInline):
    extra = 1
    model = Conference_Date_Time

class Conference_Admin(admin.ModelAdmin):
    inlines = [
        Conference_Date_Time_Inline,
        Session_Inline,
        Material_Inline,
    ]

# Register your models here.
admin.site.register(Conference, Conference_Admin)
admin.site.register(Speaks)
admin.site.register(Attendee)
admin.site.register(Purchased_Conference)
