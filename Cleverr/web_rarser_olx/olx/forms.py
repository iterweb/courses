from django import forms


class OlxForm(forms.Form):
    url = forms.URLField(label='Ссылка на рубрику', widget=forms.URLInput(
        attrs={'class': 'form-control', 'placeholder': 'Например: https://www.olx.ua/uk/transport/legkovye-avtomobili/'}
    ))

    def clean_url(self):
        data = self.cleaned_data['url']
        if not data.startswith('https://www.olx.ua/'):
            raise forms.ValidationError('Ссылка должна начинаться с "https://www.olx.ua/"')
