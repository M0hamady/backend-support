from rest_framework import serializers

from .models import Project, Step

class SteptSerializers(serializers.ModelSerializer):
    count_moshtrayat = serializers.IntegerField(source='moshtrayat_count')
    costs = serializers.IntegerField(source='all_cost')
    moshtryat = serializers.ListField(source='moshtrayat')
    class Meta:
        model = Step
        fields = "__all__"
class ProjectSerializers(serializers.ModelSerializer):
    # steps = serializers.StringRelatedField(many=True)
    step = serializers.ListField(source='steps')
    mosh = serializers.ListField(source='moshtryat')
    mosh_detail = serializers.ListField(source='moshtryat_detail')
    mettings = serializers.ListField(source='meetings')
    count_steps = serializers.IntegerField(source='steps_count')
    cost = serializers.IntegerField(source='costes')
    # stepses = serializers.StringRelatedField(source='steps')
    class Meta:
        model = Project
        fields = "__all__"

