from django import forms
from django.forms import ModelForm

from .models import Posts


# create new post
class PostForm(ModelForm):
        class Meta:
            model = Posts
            # fields = '__all__'
            fields = ('content',)
            labels = {
                'content': '',
            } 
            widgets = {
                'content': forms.Textarea(attrs={'class': 'form-control', "rows": 5,}),
            } 