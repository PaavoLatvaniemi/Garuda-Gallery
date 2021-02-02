import os.path
from django.conf import settings
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.db import models

thumbType = "thumb"
midResType = "midRes"
thumb_size = (256,512)
MidRes_size = (512,1024)

class PhotoGroup(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name


class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,
    on_delete=models.CASCADE)
    photo_group = models.ForeignKey(PhotoGroup,null=True ,on_delete=models.CASCADE, blank=True)  
    photo = models.ImageField(upload_to='photos')
    thumbnail = models.ImageField(upload_to = 'thumbnails')
    photo_MidRes = models.ImageField(upload_to = 'MidRes')
    name = models.CharField(max_length=25)
    caption = models.TextField()
    uploaded = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.make_thumbnail(thumbType):
            raise Exception('Could not create thumbnail - is the file type valid?')

        if not self.make_thumbnail(midResType):
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(Photo, self).save(*args, **kwargs)


    def make_thumbnail(self, resolutionType):
        image = Image.open(self.photo)

        thumb_name, thumb_extension = os.path.splitext(self.photo.name)
        thumb_extension = thumb_extension.lower()

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False

        if resolutionType == thumbType:
            image.thumbnail(thumb_size, Image.ANTIALIAS)
            thumb_filename = thumb_name + "_thumb" + thumb_extension

            temp_thumb = BytesIO()
            image.save(temp_thumb, FTYPE)
            temp_thumb.seek(0)

            self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)

        else:
            image.thumbnail(MidRes_size, Image.ANTIALIAS)
            thumb_filename = thumb_name + "_MidSize" + thumb_extension

            temp_thumb = BytesIO()
            image.save(temp_thumb, FTYPE)
            temp_thumb.seek(0)

            self.photo_MidRes.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)

        temp_thumb.close()
        return True