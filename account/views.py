from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def base(request):
    return render(request, 'base.html')

"""def index(request):
    return render(request, 'index.html')"""

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created, Just Login {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'registration/register.html', {'form': form})


@login_required(login_url="login")
def dashboard(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'dashboard.html', args)
@login_required(login_url="login")
def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

@login_required(login_url="login")
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You have successfully updated your profile')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile-update.html', context)


def changepasswd(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('dashboard'))
        else:
            return redirect(reverse('index'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'registration/password_change_form.html', args)
