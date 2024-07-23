from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

@login_required(login_url='login')  # Redirect to login if not authenticated
def account(request):
    try:
        profile = Profile.objects.get(user=request.user)
        items = profile.inventory.all()
        characters = profile.characters.all()
    except Profile.DoesNotExist:
        profile = None
        items = []
        characters = []

    context = {
        'profile': profile,
        'items': items,
        'characters': characters,
    }
    return render(request, 'profile_detail.html', context)

class CustomLoginView(LoginView):
    template_name = 'login.html'

def index(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('index')
