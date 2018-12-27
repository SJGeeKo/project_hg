from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

def profile_path(instance, filename):
    return 'user_profile/{}/{}'.format(instance.slug, filename)

# Create your models here.
class Painter(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique=True)
    birth = models.DateField()
    title = models.CharField(max_length=35, default='')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=profile_path, default="user_profile/profile_default_Y-6i6KZW.jpg")

    class Meta:
        ordering = ('name',)
        verbose_name = ('painter')
        verbose_name_plural = 'painters'

    def __str__(self):
        return '{}'.format(self.name)


class PainterEng(models.Model):
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=35)
    description = models.TextField(blank=True)

def painting_path(instance, filename):
    return 'painting/{}/{}/{}'.format(instance.painter.slug, instance.slug, filename)

class Painting(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    material = models.CharField(max_length = 250, default='캔버스에 유화')
    description = models.TextField(blank=True)
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE)
    width = models.DecimalField(max_digits=4, decimal_places=1)
    height = models.DecimalField(max_digits=4, decimal_places=1)
    price = models.IntegerField(default=100000)
    image = models.ImageField(upload_to=painting_path, blank=False)
    thumbnail = ImageSpecField(
        source = 'image',
        processors = [Thumbnail(350)],
        format='JPEG',
        options = {'quality': 80}
    )
    thumbnail_s = ImageSpecField(
        source = 'image',
        processors = [Thumbnail(49, 49)],
        format='JPEG',
        options = {'quality': 100}
    )
    thumbnail_detail = ImageSpecField(
        source = 'image',
        processors = [Thumbnail(680)],
        format='JPEG',
        options = {'quality': 100}
    )
    available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name = ('painting')
        verbose_name_plural = 'paintings'

    def __str__(self):
        return '{}'.format(self.name)


class PaintingEng(models.Model):
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    material = models.CharField(max_length = 250, default='Oil on canvas')
    description = models.TextField(blank=True)
    price = models.IntegerField(default=100)


def paintingImg_path(instance, filename):
    return 'painting/{}/{}/{}'.format(instance.painting.painter.slug, instance.painting.slug, filename)

class PaintingImg(models.Model):
    painting = models.ForeignKey(Painting, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=paintingImg_path, default="", blank=True)
    thumbnail = ImageSpecField(
        source = 'image',
        processors = [Thumbnail(49, 49)],
        format='JPEG',
        options = {'quality': 100}
    )
    thumbnail_detail = ImageSpecField(
        source = 'image',
        processors = [Thumbnail(680)],
        format='JPEG',
        options = {'quality': 100}
    )