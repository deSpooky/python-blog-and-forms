from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Comments:
        model = Comment
        fields = ("body")
