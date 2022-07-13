from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Debt
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum


# Create your views here.
def home(request):
    return render(request, 'home.html')

def user_home(request):
    return render(request, 'user_home.html')

def about(request):
    return render(request, 'about.html')

# Create Debt Model


'''
class Debt:
    def __init__(self, name, total, description, payment_min, interest, start_date, payment_day):
        self.name = name
        self.total = total
        self.description = description
        self.payment_min = payment_min
        self.interest = interest
        self.start_date = start_date
        self.payment_day = payment_day
        # self.end_date = end_date


Debts = [
    Debt('AES', 8000, 'student loan', 266, 4.5, '2018-08-01', '1st'),
    Debt('Sallie Mae', 6000, 'student loan', 133, 5.5, '2017-08-01', '3rd'),
    Debt('American Express', 2500, 'student loan',
         50, 13.2, '2016-08-01', '15th'),
]
'''

@login_required
def dashboard(request):
    Debts = Debt.objects.filter(user=request.user)
    totalDebt = Debt.objects.filter(user=request.user).aggregate(Sum('total'))
    return render(request, 'user/dashboard.html', {'Debts': Debts, 'totalDebt': totalDebt})

class addDebt(LoginRequiredMixin,CreateView):
    model = Debt
    fields = '__all__'
    success_url = '/dashboard/'

    def addDebt(request):
        return render(request, 'addDebt.html')

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

@login_required
def debt_details(request, Debt_id):
    Debts = Debt.objects.get(id=Debt_id)
    return render(request, 'debt/detail.html', {'Debt': Debts})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('dashboard')
    else:
        error_message = 'Invalid sign up - try again'
        # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
