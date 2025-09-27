from django import forms
from .models import Resource, Comment, Rating

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'file', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'rows': 4
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg bg-white focus:ring-2 focus:ring-blue-500 focus:outline-none'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
