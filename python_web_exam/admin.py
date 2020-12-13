from django.contrib import admin
from python_web_exam.models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','content', 'author')
    fieldsets = [
        (None, { 'fields': [('title','content', 'image')] } ),
    ]
    def save_model(self, request, obj, form, change): 
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
        # Register your models here.
admin.site.register(Posts, PostsAdmin)
