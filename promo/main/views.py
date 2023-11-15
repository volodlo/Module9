from django.shortcuts import render, redirect
from .models import *
from .forms import HumanForm, CompanyForm, HouseForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
	compan = Company.objects.all()
	house = House.objects.all()
	title = "Главная страница"
	context = {'compan': compan, 'house': house, 'title': title}
	return render(request, 'main/index.html', context)


def company(request, company_id):
	house = House.objects.filter(c=company_id)
	compan = Company.objects.all()
	humans = Human.objects.filter(c=company_id)
	current_company = Company.objects.get(pk=company_id)
	context = {'house': house, 'compan': compan, 'current_company': current_company, 'humans': humans}
	return render(request, 'main/company.html', context)


class Create_CompanyView(CreateView):
	template_name = 'main/create_company.html'
	form_class = CompanyForm
	success_url = reverse_lazy('index')

	def create_company(self, request, **kwargs):
		context = super().get_context_data(**kwargs)
		error = ''
		if request.method == 'POST':
			form = CompanyForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('index')
			else:
				error = 'Форма была неверной'
		form = CompanyForm()
		return render(request, context)


class Create_humanView(CreateView):
	template_name = 'main/create_human.html'
	form_class = HumanForm

	def create_human(self, request, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['company'] = Company.objects.all()
		error = ''
		if request.method=='POST':
			form = HumanForm(request.POST)
			if form.is_valid():
				form.save()				
			else:
				error = 'Форма была неверной'
		form = HumanForm()
		return render(request, context)


class Create_houseView(CreateView):
	template_name = 'main/create_house.html'
	form_class = HouseForm

	def create_house(self, request, **kwargs):

		context = super().get_context_data(**kwargs)
		context ['company'] = Company.objects.all()
		error = ''
		if request.method == 'POST':
			form = HouseForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('index')
		else:
			error = 'Форма была неверной'
		form = HouseForm()
		return render(request, context)


class CompanyUpdateView(UpdateView):
	model = Company
	template_name = 'main/edit_company.html'
	form_class = CompanyForm


class HumanUpdateView(UpdateView):
	model = Human
	template_name = 'main/edit_company.html'
	form_class = HumanForm


class HouseUpdateView(UpdateView):
	model = House
	template_name = 'main/edit_company.html'
	form_class = HouseForm


class CompanyDeleteView(DeleteView):
	model = Company
	success_url = '/'
	template_name = 'main/delete_company.html'
	

class HumanDeleteView(DeleteView):
	model = Human
	template_name = 'main/delete_human.html'
	success_url = '/'

class HouseDeleteView(DeleteView):
	model = House
	success_url = '/'
	template_name = 'main/delete_house.html'

