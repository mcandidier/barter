from django.conf import settings
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token


from .models import User 

class UserRegistrationSerializer(serializers.ModelSerializer):
    """ User Registration using email
    """

    confirm_password = serializers.CharField(read_only=True)

    class Meta:
        fields = ('email', 'first_name', 'last_name', 'password', 'confirm_password',)


    def validate(self, data):
        email, password, confirm_password, first_name, last_name = data.values()
        user = User.objects.filter(email=email).first()
        
        if user.exists():
            msg = _('Email has been registered already.')
            return serializers.ValidationError(msg, code='authorization')

        if confirm_password != password:
            msg = _('Password mismatch!')
            return serializers.ValidationError(msg, code='authorization')
        return data


class UserLoginSerializer(serializers.Serializer):
    """ Usere login serializer
    """
    token = None
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(UserLoginSerializer, self).__init__(*args, **kwargs)

    def validate(self, data):
        email, password = data.values()
        user = authenticate(self.request, email=email, password=password)
        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')
        self._create_token(user)
        return data

    def _create_token(self, user):
        # create token for user
        token, created = Token.objects.get_or_create(user=user)
        self.token = token.key
        return token