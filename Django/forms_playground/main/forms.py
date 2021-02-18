from django import forms
from main import models
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=256)
    #about_me = forms.TextInput()   instead of this we use
    about_me = forms.CharField(widget=forms.Textarea())

    active = forms.BooleanField()
    
class StudentForm(forms.ModelForm):
    #This is a inner abstract class used to directly inherit all fields of given model class in our StudentForm
    class Meta:
        model = models.Student
        fields = '__all__'

