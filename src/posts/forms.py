from django import forms

from .models import Post



class PostListForm(forms.ModelForm):
    """ Форма листа постов """

    class Meta:
        model = Post
        fields = '__all__'
