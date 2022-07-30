from django.shortcuts import render, get_object_or_404
from .models import Meeting, Room
from rest_framework import viewsets
from .serializers import MeetingSerializers,RoomSerializers
import requests as requests_api
from django.core.paginator import Paginator,PageNotAnInteger


# for meeting api
class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializers


# for rooms api
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


# not for api
def all_meeting(request):
    # count_meeting = Meeting.objects.count()
    # meetings = Meeting.objects.all()
    # get meeting from api
    response = requests_api.get('https://bit.ly/3PKkEBu')
    meetings = response.json()
    count_meeting = len(meetings)

    # pagination
    paginator = Paginator(meetings, 2)
    numero_page = request.GET.get('page', 1)
    try:
        meetings = paginator.page(numero_page)
    except PageNotAnInteger:
        meetings = paginator.page(1)

    return render(
        request,
        'meeting/meeting/all_meeting.html',
        {
            'count_meeting': count_meeting,
            'meetings': meetings
        }
    )


def one_meeting(requests, id):
    # meeting = get_object_or_404(Meeting, pk=id)
    response = requests_api.get('https://bit.ly/3PKkEBu')
    meetings = response.json()
    for meeting in meetings:
        if meeting['id'] == id:
            return render(
                requests,
                'meeting/meeting/one_meeting.html',
                {
                    'meeting':meeting
                }
            )


def all_room(request):
    # count_room = Room.objects.count()
    # rooms = Room.objects.all()
    response = requests_api.get('https://bit.ly/3Pwj6vl')
    rooms = response.json()
    number_room = len(rooms)
    # paginator
    paginator = Paginator(rooms, 2)
    numero_page = request.GET.get('page', 1)
    try:
        rooms = paginator.page(numero_page)
    except PageNotAnInteger:
        rooms = paginator.page(1)
    return render(
        request,
        'meeting/room/all_room.html',
        {
            'number_room': number_room,
            'rooms': rooms,
        }
    )


def one_room(requests, id):
    # room = get_object_or_404(Room, pk=id)
    response = requests_api.get('https://bit.ly/3Pwj6vl')
    rooms = response.json()

    for room in rooms:
        if room['id'] == id:
            return render(
                requests,
                'meeting/room/one_room.html',
                {'room': room}
            )
