from django.db import models
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
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