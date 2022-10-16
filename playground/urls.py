from django.urls import path
from . import views

# URLConf -- every app gets one need to add to the main urlconf
urlpatterns = [
    # call path and give it a route/url and pass a view function
    path('hello/', views.say_hello)
]
