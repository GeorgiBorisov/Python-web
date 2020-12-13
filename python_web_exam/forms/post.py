from django import forms
from python_web_exam.models import Posts

class PostsForm(forms.ModelForm):
    title = forms.CharField(min_length=3, max_length=50, required=True)
    content = forms.Textarea(attrs={'required': True})
    image = forms.ImageField(required=False)
    class Meta:
        model = Posts
        fields = ['title', 'content', 'image', 'author']
        widget = {'author': forms.CharField()}
        
