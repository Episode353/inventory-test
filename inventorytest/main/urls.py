from django.urls import path
from .views import account, CustomLoginView, index, logout_view

urlpatterns = [
    path('', index, name="index"),
    path('profiles/', account, name='account'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    
]
