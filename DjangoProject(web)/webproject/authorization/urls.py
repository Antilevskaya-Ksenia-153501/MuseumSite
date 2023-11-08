from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegistrationEmployeeForm.as_view(), name='registerEmployee'),
    path('signup/user', views.RegistrationCustomerForm.as_view(), name='registerCustomer'),
    path('signin/', views.SignInForm.as_view(), name='signin'),
    path('logout/', views.LogoutForm.as_view(), name='logout')
]