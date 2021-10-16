from rest_framework import  serializers
from accounts.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'phone_number','individual','business','password']