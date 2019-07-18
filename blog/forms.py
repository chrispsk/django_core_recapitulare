from django import forms
from .models import PostModel
from django.core.exceptions import ValidationError

class PostModelForm(forms.ModelForm):
    # Not good practice
    # title = forms.CharField(max_length=20, error_messages={
    #     'required': "The title field is required!!!!"
    # })
    # VALIDATION METHOD 1 don't need to be in model
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError("Title too short!!!!")
        return title
    #
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) < 2:
            raise forms.ValidationError("Content Nope")
        return content


    class Meta:
        model = PostModel
        fields = [
            'title',
            'content'
        ]
        # VALIDATION METHOD 2 Must be in models
        error_messages={
            "title": {
                # "max_length": "This is too long" #this won't happen
                "required": "Title required!!!", # Apare daca bag spaces
            },
            "content": {
                "required": "Content required!!!", # Apare daca e required from model
            }
        }
