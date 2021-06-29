from django import forms
from .models import News
import re #модуль для работы с регулярными выражениями
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
#from .models import Category


class ContactForm(forms.Form):
	subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
	content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
	captcha = CaptchaField(label='Каптча')


class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label='Имя пользователя', help_text='Имя пользователя писать сюда', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
	username = forms.CharField(label='Имя пользователя', help_text='Имя пользователя писать сюда', widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


# форма не связанная с моделью
'''
class NewsForm(forms.Form):
	title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
	content = forms.CharField(required=False, label='Текст', widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})) # required=False не обязательно к заполнению
	is_published = forms.BooleanField(initial=True, label='Опубликовано')
	category = forms.ModelChoiceField(empty_label='Выберите категорию', queryset=Category.objects.all(), label='Категория', widget=forms.Select(attrs={"class": "form-control"}))
'''

# форма связанная с моделью	
class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		#fields = '__all__'
		fields = ['title', 'content', 'is_published', 'category']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
			'category': forms.Select(attrs={'class': 'form-control'})
		}
	# функция валидатор		
	def clean_title(self): 
		title = self.cleaned_data['title']
		if re.match(r'\d', title):
			raise ValidationError('Название не должно начинаться с цифры')
		return title