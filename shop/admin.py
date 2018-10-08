from django.contrib import admin
from .models import Painter, Painting

# Register your models here.
class PainterAdmin(admin.ModelAdmin):
    list_display=['name', 'birth']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Painter, PainterAdmin)

class PaintingAdmin(admin.ModelAdmin):
    list_display=['name','painter','price','available']
    list_editable=['price','available','painter']
    prepopulated_fields={'slug':('name',)}
    list_per_page=20

admin.site.register(Painting, PaintingAdmin)