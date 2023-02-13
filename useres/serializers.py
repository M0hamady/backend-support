from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from  .models import  User as User_inf
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    info = serializers.ListField(source='inf')
    projects = serializers.ListField(source='projec')
    last_project_percent = serializers.IntegerField(source='project_percent')
    projec_steps = serializers.ListField(source='projec_step')
    numper_of_finished_project = serializers.IntegerField(source='numper_of_finished_projects')
    class Meta:
        model = User_inf
        fields = "__all__"
class UserSerializersMin(serializers.ModelSerializer):
    info = serializers.ListField(source='inf')
    projects = serializers.ListField(source='projec')
    last_project_percent = serializers.IntegerField(source='project_percent')
    numper_of_finished_project = serializers.IntegerField(source='numper_of_finished_projects')

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

    number = serializers.CharField(write_only=True, required=True, )
    password2 = serializers.CharField(write_only=True, required=True,)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name',"number")
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    def validate_number(self, val):
        if '010' or '015' or '011' or '012'  in val[0:3]:
            return val
        raise serializers.ValidationError("error message")

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
        user_inf = User_inf.objects.create(
            user = user,
            phone =validated_data['number']
        )
        user_inf.save()

        return user
class User_Serualizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ChangeImagwSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_inf
        fields = "__all__"