from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('debt/', views.addDebt, name='addDebt' ),
    path('debt/<int:Debt_id>/', views.debt_details, name='debt_details'),
]
