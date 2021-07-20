from django.urls import path
  
from videoApp.views import VideoListView, VideoView, VideoStreamView

urlpatterns = [
    path("", VideoListView.as_view(), name="home"),
    path("video/<int:pk>/", VideoView.as_view(), name="video"),
    path("video/stream/<int:pk>/", VideoStreamView, name="stream")
]
