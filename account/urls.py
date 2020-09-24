from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('',  HomeView.as_view(), name='home'),
]
