from django import forms

from webapp.models import Package, Address


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['address', 'title', 'weight', 'link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'address': 'Адрес',
            'title': 'Название посылки',
            'weight': 'Вес (кг)',
            'link': 'Ссылка на товар',
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('name', 'city', 'country', 'postal_code')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Адрес',
            'city': 'Город',
            'country': 'Страна',
            'postal_code': 'Почтовый индекс',
        }
