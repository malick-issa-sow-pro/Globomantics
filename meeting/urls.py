from django.urls import path, include
from . import views
from rest_framework import routers
from .views import MeetingViewSet, RoomViewSet

# for api
router = routers.DefaultRouter()
router.register(r'meetings', MeetingViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('', views.all_meeting, name='all_meeting'),
    path('<int:id>', views.one_meeting, name='one_meeting'),
    path('rooms/', views.all_room, name='all_room'),
    path('rooms/<int:id>', views.one_room, name='one_room'),
    # for api
    path('api/', include(router.urls)),
]
