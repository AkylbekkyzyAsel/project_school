from django.shortcuts import render
from django.views import generic
from .models import Student
from .forms import StudentForm

class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student.html'



