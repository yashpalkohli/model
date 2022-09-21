from dataclasses import fields
from django import forms
from .models import Page,Post,Song

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields= "__all__"

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= "__all__"

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields= "__all__"


