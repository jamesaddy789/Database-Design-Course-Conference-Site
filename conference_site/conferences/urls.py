from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Login', views.login_request, name='login'),
    path('Logout', views.logout_request, name='logout'),
    path('Register', views.register, name='register'),
    path('browse_conferences', views.browse_conferences, name='browse_conferences'),
    path('conference_detail=<int:pk>', views.conference_detail, name='conference_detail'),
    path('conference_checkout=<int:pk>=<str:current_price>', views.conference_checkout, name='conference_checkout'),
    path('view_bill', views.view_bill, name='view_bill'),
    path('checkout_confirmation=<int:pk>=<str:price>', views.checkout_confirmation, name='checkout_confirmation')
]
