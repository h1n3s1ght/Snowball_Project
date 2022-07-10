from django.shortcuts import render
from django.http import HttpResponse
from .models import Debt

# Create your views here.
def home(request):
    return render(request, 'home.html')

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
    Debt('American Express', 2500, 'student loan', 50, 13.2, '2016-08-01', '15th'),
]
'''

def dashboard(request):
    Debts = Debt.objects.all()
    return render(request, 'user/dashboard.html', {'Debts': Debts})

def addDebt(request):
    return render(request, 'user/addDebt.html')

def debt_details(request, Debt_id):
    Debts = Debt.objects.get(id=Debt_id)
    return render(request, 'debt/detail.html', {'Debt': Debts})