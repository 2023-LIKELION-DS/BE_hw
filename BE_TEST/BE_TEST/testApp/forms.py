from django import forms
from .models import Basic
class PostBaseForm(forms.Form):
    title=forms.CharField()
    comment=forms.CharField(widget=forms.Textarea)

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Basic
        fields = '__all__'

from django.core.exceptions import ValidationError
class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['title', 'content']
    
    def clean_content(self):
        data = self.cleaned_data['content']
        if "비속어" == data:
            raise ValidationError("'비속어'는 사용하실 수 없습니다.")

        return data