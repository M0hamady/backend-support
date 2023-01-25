from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from  .models import  User as User_inf
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    info = serializers.ListField(source='inf')
    projects = serializers.ListField(source='projec')
    last_project_percent = serializers.IntegerField(source='project_percent')
    class Meta:
        model = User_inf
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:

            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_firstname(self, name_val):
        if 'ann' not in name_val.lower():
            raise serializers.ValidationError("error message")

        return name_val

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
class User_Serualizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"