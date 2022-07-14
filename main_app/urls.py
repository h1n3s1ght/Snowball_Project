from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home/', views.user_home, name='user_home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('debt/create/', views.addDebt.as_view(), name='addDebt' ),
    path('debt/<int:Debt_id>/', views.debt_details, name='debt_details'),
    path('accounts/signup/', views.signup, name='signup'),
    path('debt/<int:pk>/update/', views.DebtUpdate.as_view(), name='debt_update'),
    path('debt/<int:pk>/delete/', views.DebtDelete.as_view(), name='debt_delete'),
]
