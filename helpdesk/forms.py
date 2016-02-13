from django import forms

class NewComment(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

class NewTopicForPas(forms.Form):
    CHOICES = (
        ('', ''),
    )

    department = forms.ChoiceField(choices=CHOICES, required=True, label='Subject')

    content = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, departments=None, *args, **kwargs):
        super(NewTopicForPas, self).__init__(*args, **kwargs)
        if departments:
            self.fields['department'].choices = departments

class NewTopicForPdi(forms.Form):

    CHOICES = (
        ('', ''),
    )

    subject = forms.ChoiceField(choices=CHOICES, required=True, label='Subject')

    content = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, subjects=None, *args, **kwargs):
        super(NewTopicForPdi, self).__init__(*args, **kwargs)
        if subjects:
            self.fields['subject'].choices = subjects

class TeacherChooser(forms.Form):

    CHOICES = (
        ('', ''),
    )

    teacher = forms.ChoiceField(choices=CHOICES, required=True, label='Teacher')

    def __init__(self, teachers=None, *args, **kwargs):
        super(NewTopicForPdi, self).__init__(*args, **kwargs)
        if teachers:
            self.fields['teacher'].choices = teachers



