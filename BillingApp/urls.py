from django.urls import path
from . import views

app_name = 'BillingApp'

urlpatterns = [
	path('', views.calculate_cgpa, name = 'calulate_cgpa'),
	path('result/', views.show_cgpa, name = 'show_cgpa'),
]