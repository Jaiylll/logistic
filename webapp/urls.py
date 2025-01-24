from django.urls import path

from webapp.views import index, PackageListView, PackageCreateView, AddressCreateView

app_name = 'webapp'

urlpatterns = [
    path('', index, name='index'),
    path('profile/', PackageListView.as_view(), name='profile'),
    path('create/', PackageCreateView.as_view(), name='create_package'),
    path('create/address/', AddressCreateView.as_view(), name='create_address'),
]
