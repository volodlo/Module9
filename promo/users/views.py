from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import ProfileCreationForm, ProfileChangeForm, LoginUserForm
from .models import ProfileUser


class SignUpView(CreateView):
    form_class = ProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def profile(request, current_user):
    profile_user = ProfileUser.objects.all()
    current_user_id = ProfileUser.objects.get(pk=current_user)
    title = "Мой профиль"
    context = {'profile_user': profile_user, 'current_user_id': current_user_id, 'title': title}
    return render(request, 'users/profile.html', context)

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

class UserUpdateView(UpdateView):
    model = ProfileUser
    template_name = 'users/edit_profile.html'
    form_class = ProfileChangeForm


def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/password.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password.html', {'form': form})
