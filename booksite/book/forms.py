from .models import Profile
from django.forms import ModelForm
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