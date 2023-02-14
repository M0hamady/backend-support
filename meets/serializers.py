from datetime import datetime

from djoser.conf import User
from rest_framework import serializers

from .models import  Meet


class MeetingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meet
        fields = "__all__"
        extra_kwargs = {
            'location': {'required': True},
            'number': {'required': True},
            'meet_at': {'required': True},
            'meet_time': {'required': True},
            'user': {'required':True,},
            'name': {'required':False,},

        }

    def validate_meet_at (self, meet_at):
        if meet_at == "" :
            raise serializers.ValidationError("can not be null")
        elif meet_at < datetime.today().date():
            raise  serializers.ValidationError("meet does not before today")
        else:
            return meet_at

    def create(self, validated_data):
        # user_get = validated_data['username']
        # user = User.objects.get(username = user_get)
        print(datetime.today().date())
        meet =Meet.objects.create(
            location=validated_data['location'],
            number = validated_data['number'],
            meet_at = validated_data['meet_at'],
            meet_time =validated_data['meet_time'],
            user = validated_data['user'],
            name =f'nmaE'
        )

        return meet