from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientView.as_view(), name='clients_list'),
    path('<int:pk>/', views.DetailAccountView.as_view(), name='detail_client'),
    path('<int:pk>/credit', views.DetailCreditView.as_view(), name='detail_credit'),
]