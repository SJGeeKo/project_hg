from django.contrib import admin
from .models import Painter, PainterEng, Painting, PaintingEng, PaintingImg

# Register your models here.
class PainterInline(admin.StackedInline):
    model = PainterEng
    extra = 1

class PainterAdmin(admin.ModelAdmin):
    inlines = [PainterInline,]
    list_display=['name', 'birth']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Painter, PainterAdmin)

class PaintingImgInline(admin.TabularInline):
    model = PaintingImg
    extra = 3

class PaintingEngInline(admin.StackedInline):
    model = PaintingEng
    extra = 1

class PaintingAdmin(admin.ModelAdmin):
    inlines = [PaintingImgInline, PaintingEngInline]
    readonly_fields = ('date_added',)
    list_display=['name','painter','price','available']
    list_editable=['price','available','painter']
    prepopulated_fields={'slug':('name',)}
    list_per_page=20

admin.site.register(Painting, PaintingAdmin)