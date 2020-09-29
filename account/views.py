from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserRegistrationSerializer, UserLoginSerializer

class HomeView(TemplateView):

    template_name = 'account/facebook_login.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        pass

class UserLoginView(APIView):
    """ User login API view
    """ 
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    
    def post(self, *args, **kwargs):
        serializer = self.serializer_class(
            data=self.request.data,
            request=self.request
            )
        serializer.is_valid(raise_exception=True)
        return Response({
            'token': serializer.token,
        }, status=200)


class UserAuthViewset(ViewSet):
    """ User Registration using email
    """
    permission_classes = (AllowAny, )
    serializer_class = UserRegistrationSerializer
    
    def user_signup(self, *args, **kwargs):
        serializer = UserRegistrationSerializer(
            data=self.request.data,
            request=self.request)
        pass


class UserViewSet(ViewSet):
    """ Authenticated user views
    """ 
    permission_classes = (IsAuthenticated,)

    def user_info(self, *args, **kwargs):
        pass

    def user_logout(self, *args, **kwargs):
        pass


    def user_update(self, *args, **kwargs):
        pass

