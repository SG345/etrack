from rest_framework import serializers

from api.models import Log, BlockedEvents


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('UserDevice', 'EventName', 'EventLabel', 'EventAction', 'EventTime')

class BlockedEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedEvents
        fields = ('EventName', 'Counter')
