from django.urls import path
from .views import profile_list, CustomLoginView, index
urlpatterns = [
    path('', index, name="index"),
    path('profiles/', profile_list, name='profile_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    
]
