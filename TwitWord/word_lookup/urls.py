from django.urls import path

from . import views

# The home view
urlpatterns = [
    path('', views.home, name='home'),
    path('<word>/', views.word_input, name='word_input'),
]