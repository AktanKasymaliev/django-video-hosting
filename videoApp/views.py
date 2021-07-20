from django.shortcuts import get_object_or_404, render
from django.views import generic

from videoApp.models import Video

class VideoListView(generic.View):

    def get(self, request):
        return render(
            request, 
            "videoApp/home.html", 
            {"videos": Video.objects.all()}
            )

class VideoView(generic.View):
    
    def get(self, request, pk):
        return render(
            request,
            "videoApp/video.html",
            {"video": get_object_or_404(Video, pk=pk)}
        )