from django import forms
from .models import student
#DataFlair
class  StudentCreate(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'