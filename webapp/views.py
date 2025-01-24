from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from webapp.forms import PackageForm, AddressForm
from webapp.models import Package, Address


def index(request):
    # volume = None
    # weight = None
    # if request.method == 'POST':
    #     volume = float(request.POST.get('volume', 0))
    #     weight = float(request.POST.get('weight', 0))
    #     if not volume or not weight:
    #         error = 'Объем и вес должны быть заполнены'
    #         return render(request, 'index.html', {'error': error})
    #     if volume < 0 or weight < 0:
    #         error = 'Не принимаются значения меньше 0'
    #         return render(request, 'index.html', {'error': error})
    #     price = (volume + weight) * 3.1
    #     return JsonResponse({'price': price, 'volume': volume, 'weight': weight}, status=200)
    return render(request, 'index.html')


class PackageListView(ListView):
    model = Package
    context_object_name = 'packages'
    template_name = 'packages/packages-list.html'

    def get_queryset(self):
        return super().get_queryset().filter(address__owner=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Address.objects.filter(owner=self.request.user).order_by('name')
        return context


class PackageCreateView(CreateView):
    model = Package
    form_class = PackageForm
    template_name = 'packages/package_create.html'

    def get_success_url(self):
        return reverse('webapp:profile')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['address'].queryset = Address.objects.filter(owner=self.request.user)
        return form


class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'packages/package_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return redirect(reverse('webapp:profile'))
