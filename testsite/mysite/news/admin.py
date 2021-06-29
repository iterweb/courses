from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
	form = NewsAdminForm
	list_display = ('id', 'views', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
	list_display_links = ('id', 'title')
	search_fields = ('title', 'content')
	list_editable = ('is_published',)
	list_filter = ('is_published', 'category')
	fields = ('id', 'title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'created_at', 'updated_at',)
	readonly_fields = ('id', 'get_photo', 'created_at', 'updated_at',)

	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo.url}" width="50">')
		else:
			return 'Нет фото'

	get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')
	list_display_links = ('id', 'title')
	search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)	

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'