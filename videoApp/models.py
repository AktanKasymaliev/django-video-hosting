from django.db import models
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images")
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "video"

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.CharField(max_length=100)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="video")
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return f"Comment by {self.user}"
