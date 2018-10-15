from django.db import models

# Create your models here.
class Painter(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique=True)
    birth = models.DateField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='user_profile', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = ('painter')
        verbose_name_plural = 'painters'

    def __str__(self):
        return '{}'.format(self.name)

class Painting(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    material = models.CharField(max_length = 250, default='Oil')
    description = models.TextField(blank=True)
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE)
    width = models.IntegerField(default=10)
    height = models.IntegerField(default=10)
    price = models.IntegerField(default=100000)
    image = models.ImageField(upload_to='painting', blank=False)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = ('painting')
        verbose_name_plural = 'paintings'

    def __str__(self):
        return '{}'.format(self.name)