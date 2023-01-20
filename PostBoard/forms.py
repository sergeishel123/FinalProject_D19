from django import forms
from .models import Post,Category


class PostForm(forms.ModelForm):
    category = forms.CharField(max_length = 64)
    class Meta:
        model = Post
        fields = (
            'heading',
            'text',
            'cover',
        )

