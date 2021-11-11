from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'school', 'is_active', 'is_graduated']

