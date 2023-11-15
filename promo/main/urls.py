from django.urls import path
from .import views
from .views import *


urlpatterns = [
	path('', views.index, name='index'),

	path('company/<int:company_id>/', company, name='company'),

	path('create_company', Create_CompanyView.as_view(), name='create_company'),
	path('create_human', Create_humanView.as_view(), name='create_human'),
	path('create_house', Create_houseView.as_view(), name='create_house'),
	
	path('edit_company/<int:pk>/', views.CompanyUpdateView.as_view(), name='edit_company'),
	path('company/<int:pk>/edit_human', views.HumanUpdateView.as_view(), name='edit_human'), 
	path('company/<int:pk>/edit_house', views.HouseUpdateView.as_view(), name='edit_house'), 

	path('delete_company/<int:pk>/', views.CompanyDeleteView.as_view(), name='delete_company'),
	path('company/<int:pk>/delete_human', views.HumanDeleteView.as_view(), name='delete_human'), 
	path('company/<int:pk>/delete_house', views.HouseDeleteView.as_view(), name='delete_house'),
]
