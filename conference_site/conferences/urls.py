from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('register', views.register, name='register'),
    path('confirm_registration', views.confirm_registration, name='confirm_registration'),
    path('browse_conferences', views.browse_conferences, name='browse_conferences'),
    path('conference_detail=<int:pk>', views.conference_detail, name='conference_detail'),
    path('conference_checkout=<int:pk>=<str:current_price>', views.conference_checkout, name='conference_checkout'),
    path('view_bill', views.view_bill, name='view_bill'),
    path('account_info', views.account_info, name='account_info'),
    path('update_account_info', views.update_account_info, name='update_account_info'),
    path('change_password', views.change_password, name='change_password'),
    path('change_password_confirmation', views.change_password_confirmation, name='change_password_confirmation'),
    path('checkout_confirmation=<int:pk>=<str:price>', views.checkout_confirmation, name='checkout_confirmation'),
    path('remove_purchase=<int:pk>', views.remove_purchase, name='remove_purchase'),
    path('remove_purchase_confirmation=<str:purchase_name>', views.remove_purchase_confirmation, name='remove_purchase_confirmation'),
]
