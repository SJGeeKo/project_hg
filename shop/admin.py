from django.contrib import admin
from .models import Painter, Painting, PaintingImg

# Register your models here.
class PainterAdmin(admin.ModelAdmin):
    list_display=['name', 'birth']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Painter, PainterAdmin)

class PaintingImgInline(admin.TabularInline):
    model = PaintingImg
    extra = 3

class PaintingAdmin(admin.ModelAdmin):
    inlines = [PaintingImgInline,]
    readonly_fields = ('date_added',)
    list_display=['name','painter','price','available']
    list_editable=['price','available','painter']
    prepopulated_fields={'slug':('name',)}
    list_per_page=20

admin.site.register(Painting, PaintingAdmin)