
from django.shortcuts import render
from .models import Profile, Item, Set, Bundle, Character

def profile_list(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        context = {
            'profile': profile,
            'items': profile.inventory.all(),
            'characters': profile.characters.all(),
        }
        return render(request, 'profile_detail.html', context)
    else:
        profiles = Profile.objects.all().prefetch_related('inventory', 'characters')
        items = Item.objects.all()
        sets = Set.objects.all()
        bundles = Bundle.objects.all()
        characters = Character.objects.all()

        context = {
            'profiles': profiles,
            'items': items,
            'sets': sets,
            'bundles': bundles,
            'characters': characters,
        }
        return render(request, 'profile_list.html', context)


from django.contrib.auth.views import LoginView

# Your existing imports and views

class CustomLoginView(LoginView):
    template_name = 'login.html'



# Create your views here.
def index(request):
    return render(request, 'test1.html')