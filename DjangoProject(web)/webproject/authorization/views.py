from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import EmployeeCreateForm, CustomerCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class RegistrationEmployeeForm(FormView):
    form_class = EmployeeCreateForm
    success_url = '/auth/signin/'

    template_name = 'register.html'

    def form_valid(self, form):
        form.save(True)
        return super(RegistrationEmployeeForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationEmployeeForm, self).form_invalid(form)


class RegistrationCustomerForm(FormView):
    form_class = CustomerCreateForm
    success_url = '/auth/signin/'

    template_name = 'register.html'

    def form_valid(self, form):
        form.save(True)
        return super(RegistrationCustomerForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationCustomerForm, self).form_invalid(form)


class SignInForm(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'signin.html'

    def get(self, request):
        return render(request, 'signin.html', {'form': self.form_class})

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(SignInForm, self).form_valid(form)


class LogoutForm(FormView):
    def get(self, request):
        logout(request)
        return redirect('/')