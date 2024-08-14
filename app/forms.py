from django import forms
from app.models import *

class TopicForm(forms.Form):
    topicname=forms.CharField(max_length=50)

class WebpageForm(forms.Form):
    topicname=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    email=forms.EmailField()

class AccessForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    author=forms.CharField(max_length=50)
    date=forms.DateField()


class TopicModelForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'
        


class WebpageModelForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'

class AccessModelForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'
    