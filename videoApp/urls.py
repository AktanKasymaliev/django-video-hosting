from django.urls import path
  
from videoApp.views import VideoListView, VideoView

urlpatterns = [
    path("", VideoListView.as_view(), name="home"),
    path("video/<int:pk>/", VideoView.as_view(), name="video")
]
