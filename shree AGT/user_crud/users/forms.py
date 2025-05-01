from django import forms
from .models import User

class UserForm(forms.ModelForm):
    hobbies = forms.MultipleChoiceField(
        choices=[
            ('Reading', 'Reading'),
            ('Sports', 'Sports'),
            ('Music', 'Music'),
            ('Traveling', 'Traveling'),
        ],
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = User
        fields =  ['username', 'first_name', 'last_name', 'email', 'phone', 'gender', 'hobbies','dob'
        ]
    
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.hobbies = ", ".join(self.cleaned_data['hobbies'])
        if commit:
            user.save()
        return user