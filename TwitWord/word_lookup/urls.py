from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # The home view
    path('', views.home, name='home'),
    # The word view
    path('tweets/<user_id>', views.word_input, name='word_input'),
    path('<any>' , RedirectView.as_view(url='/', permanent=True)),
]