from .models import Profile, Chapter
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    def clean(self):
        cleaned_data=super().clean()
        print(cleaned_data)
        answers=cleaned_data.get("answers")
        print(answers.count())
        for n in range(0,answers.all().count()):

            for b in range(0, answers.all().count()):
                if answers.all()[n].chapter==answers.all()[b].chapter and b !=n:

                    raise ValidationError('only one answer per chapter')

class ChapterForm(ModelForm):
    class Meta:
        model=Chapter
        fields = '__all__'
    field1 = forms.ModelChoiceField(queryset=None, empty_label="(Nothing)")
    def __init__(self, *args, **kwargs):
        mario=kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
        self.fields['field1'].queryset=mario.profile.answers
        #forms.ModelChoiceField(queryset=kwargs.pop('user',None), empty_label="(Nothing)")
        print('aaaaaaaaaaargs',kwargs)
        
    #self.fields['field1'].queryset = self.request.user.profile

    
    #mario1 = forms.CharField()


