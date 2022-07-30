from rest_framework import serializers
from .models import Meeting, Room


class MeetingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'title_meeting', 'duration', 'start_time', 'date_meeting', 'room')


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name_room', 'floor', 'number_of_room')
