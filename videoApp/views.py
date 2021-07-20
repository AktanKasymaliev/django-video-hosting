from django.http.response import StreamingHttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from videoApp.stream import VideoStream
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
    
def VideoStreamView(request, pk):
    video_stream = VideoStream()
    file, status_code, content_length, content_range = video_stream.open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    # Headers for front-end
    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

#TODO 1 Сделать пагинацию homeview. 2 Сделать html для video.html. 3 Сделать систему комментов с django_channels