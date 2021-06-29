# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from .utils import MyMixin


def mail(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			m_mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'exemple@gmail.com', ['exemple@ukr.net'], fail_silently=False)
			if m_mail:
				messages.success(request, 'Письмо отправлено')
				return redirect('mail')
			else:
				messages.error(request, 'Ошибка отправки')
		else:
			messages.error(request, 'Ошибка валидации')
	else:
		form = ContactForm()

	return render(request, 'news/email.html', {'form': form})


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user) #моментатьгая авторизация
			messages.success(request, 'Вы зарегистрировались')
			return redirect('home')
		else:
			messages.error(request, 'Ошибка регистрации')
	else:
		form = UserRegisterForm()
	context = {
		'form': form,
	}
	return render(request, 'news/register.html', context)


def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('home')
	else:
		form = UserLoginForm()
	return render(request, 'news/login.html', {'form': form})


def user_logout(request):
	logout(request)
	return redirect('home')	


class HomeNews(MyMixin, ListView): # по умолчанию _list.html
	model = News
	template_name = 'news/index.html'
	context_object_name = 'news'
	queryset = News.objects.filter(is_published=True).select_related('category')
	paginate_by = 2

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.get_upper('Главная')
		return context
'''
	def get_queryset(self):
		return News.objects.filter(is_published=True).select_related('category')
'''

'''
def index (request):
	news = News.objects.all()
	context = {
	    'news': news,
	    'title': 'Главная',
	}
	return render(request, 'news/index.html', context)
'''


class NewsByCategory(MyMixin, ListView):
	model = News
	template_name = 'news/category.html'
	context_object_name = 'news'
	allow_empty = False # не показавыет пустые категории
	paginate_by = 2

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
		return context

	def get_queryset(self):
		return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

		
'''
def get_category(request, category_id):
	news = News.objects.filter(category_id=category_id)
	category = Category.objects.get(pk=category_id)
	context = {
	    'news': news,
	    'category': category,
	}
	return render(request, 'news/category.html', context)
'''

class NewsDetail(DetailView): # по умолчанию _detail.html
	model = News
	#pk_url_kwarg = 'news_id'
	#template_name = 'news/view_news.html'
	#context_object_name = 'news_item'


'''
def view_news(request, news_id):
	#news_item = News.objects.get(pk=news_id)
	news_item = get_object_or_404(News, pk=news_id)
	context = {
		'news_item': news_item,
	}
	return render(request, 'news/view_news.html', context)
'''
# функция формы не связанной с моделью
'''
def add_news(request):
	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			#print(form.cleaned_data)
			news = News.objects.create(**form.cleaned_data)
			return redirect(news)
	else:
		form = NewsForm()
	context = {
		'form': form
	}
	return render(request, 'news/add_news.html', context)
'''
'''
# функция формы не связанной с моделью
def add_news(request):
	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			news = form.save()
			return redirect(news)
	else:
		form = NewsForm()
	context = {
		'form': form,
	}
	return render(request, 'news/add_news.html', context)
	'''

class CreateNews(LoginRequiredMixin, CreateView):
	form_class = NewsForm
	template_name = 'news/add_news.html'
	#success_url = reverse_lazy('home')
	raise_exception = True # вызов 403 ошибки
	#login_url = '/admin/' #  перенаправление на страницу
