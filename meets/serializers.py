from datetime import datetime

from djoser.conf import User
from rest_framework import serializers

from .models import  Meet


class MeetingSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = Meet
        fields = "__all__"
        extra_kwargs = {
            'location': {'required': True},
            'number': {'required': True},
            'meet_at': {'required': True},
            'meet_time': {'required': True},
            'user': {'required':False,},
            'name': {'required':False,},

        }


    def create(self, validated_data):
        user_get = validated_data['username']
        user = User.objects.get(username = user_get)
        print(datetime.today())
        Meet.objects.create(
            location=validated_data['location'],
            number = validated_data['number'],
            meet_at = validated_data['meet_at'],
            meet_time =validated_data['meet_time'],
            user = user,
            name =f'nmaE'
        )
