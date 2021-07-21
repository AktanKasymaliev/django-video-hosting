from django.http.response import StreamingHttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from videoApp.funcs import make_pagination
from videoApp.stream import VideoStream
from videoApp.models import Comments, Video

class VideoListView(generic.View):

    def get(self, request):
        all_data = Video.objects.all()
        context = make_pagination(
            request, all_data, {}, 'videos', 8)
        return render(
            request, 
            "videoApp/home.html", 
            context
            )

class VideoView(generic.View):
    
    def get(self, request, pk):
        videos = get_object_or_404(Video, pk=pk)
        return render(
            request,
            "videoApp/video.html",
            {"video": videos, "comments": Comments.objects.filter(video=videos)}
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

#TODO 3 доделать баг с consumers