from django import forms
from .models import *
from django.forms import ModelChoiceField

class NewComment(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

class NewTopicForPas(forms.Form):

    title = forms.CharField()

    priority = forms.ChoiceField(choices=PRIORITY_OPTIONS, required=True, label='Priority')

    content = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        try:
            dynamic_choices = kwargs.pop('dynamic_choices')
        except KeyError:
            dynamic_choices = None # if normal form
        super(NewTopicForPdi, self).__init__(*args, **kwargs)
        if dynamic_choices is not None:
            self.fields['department'] = ModelChoiceField(
                                          queryset=dynamic_choices)
    class Meta:
        model = Department

class NewTopicForPdi(forms.Form):

    def __init__(self, *args, **kwargs):
        try:
            dynamic_choices = kwargs.pop('dynamic_choices')
        except KeyError:
            dynamic_choices = None # if normal form
        super(NewTopicForPdi, self).__init__(*args, **kwargs)
        if dynamic_choices is not None:
            self.fields['subject'] = ModelChoiceField(
                                          queryset=dynamic_choices)

    title = forms.CharField()

    priority = forms.ChoiceField(choices=PRIORITY_OPTIONS, required=True, label='Priority')

    content = forms.CharField(widget=forms.Textarea, required=True)

    subject = forms.ModelChoiceField(queryset=None)

    class Meta:
        model = Subject

class TeacherChooser(forms.Form):

    CHOICES = (
        ('', ''),
    )

    teacher = forms.ChoiceField(choices=CHOICES, required=True, label='Teacher')

    def __init__(self, teachers=None, *args, **kwargs):
        super(NewTopicForPdi, self).__init__(*args, **kwargs)
        if teachers:
            self.fields['teacher'].choices = teachers



