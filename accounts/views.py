from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Аккаунт успешно создан! Теперь вы можете войти.')
        return response

class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    
    def post(self, request):
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {user.first_name}!')
                return redirect('home')
        return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта.')
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
