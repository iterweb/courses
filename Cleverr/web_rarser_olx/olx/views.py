from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView, View

from .models import OlxAdvert
from .forms import OlxForm
from .utils import OlxParser


class IndexView(ListView):
    model = OlxAdvert
    template_name = 'olx/index.html'
    context_object_name = 'adverts'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'OLX Парсер'
        context['form'] = OlxForm
        return context


class ParserView(View):
    form_class = OlxForm
    parser = OlxParser()

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            url = request.POST.get('url')
            self.parser.main(url)
            messages.success(request, 'Парсинг закончен!')
            return redirect('olx:home')
        else:
            messages.error(request, 'Неверные данные! Ссылка должна начинаться с "https://www.olx.ua/"')
            return redirect('olx:home')
