from django.core import validators
from django import forms
def check_for_q(value):
    if value[0].upper()=='Q':
        raise forms.ValidationError('started with Q')
def check_for_len(v):
    if len(v)<=5:
        raise forms.ValidationError('len is < than 5')

class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_q,validators.MaxLengthValidator(7)])
    fathername=forms.CharField(max_length=100,validators=[check_for_q])
    email=forms.EmailField()
    reemail=forms.EmailField()
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reemail']
        if e!=r:
            raise forms.ValidationError('emails not matched')
    
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot catched')
    



