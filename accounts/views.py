from django.contrib.auth import logout, get_user_model, authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from accounts.forms import UserRegistrationForm, LoginForm

User = get_user_model()


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
