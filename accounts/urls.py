from django.urls import path

from accounts.views import logout_view, RegisterView, login_view

app_name = 'accounts'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),

]
