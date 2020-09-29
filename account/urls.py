from django.urls import path, include

from .views import HomeView, UserLoginView

urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('login/', UserLoginView.as_view(), name='login'),
    path('',  HomeView.as_view(), name='home'),
]
