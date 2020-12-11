from django import forms
from python_web_exam.models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        # fields = '__all__'
        fields = ['title', 'content', 'image', 'author']
        widget = {'author': forms.TextInput()}