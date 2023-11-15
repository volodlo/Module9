from .models import *
from django.forms import ModelForm


class HumanForm(ModelForm):
	class Meta:
		model = Human
		fields = ["name", "surname","mail","telephone", "c"]


class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = ["name_company"]
		

class HouseForm(ModelForm):
	class Meta:
		model = House
		fields = ("city", "street", "house_number", "c")

