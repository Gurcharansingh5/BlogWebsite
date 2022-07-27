from django.contrib import admin
from . models import *
# Register your models here.

class blogss(admin.ModelAdmin):
    list_display = ('id','title','description','date','blodid','post_views')
admin.site.register(Blogs,blogss)

class comments(admin.ModelAdmin):
    list_display = ('id','blogname','commentatorname','commentonblog','date')
admin.site.register(comment,comments)