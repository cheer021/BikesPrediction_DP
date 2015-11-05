from rest_framework import serializers

from bikesmtl.models import Station, StationDataNow


class StationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Station


class StationDataNowSerializer(serializers.ModelSerializer):
    station = StationSerializer(required=False)

    class Meta:
        model = StationDataNow