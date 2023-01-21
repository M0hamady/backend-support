from rest_framework import serializers

from .models import Websiteindex

class Website_Serualizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Websiteindex
        fields = "__all__"