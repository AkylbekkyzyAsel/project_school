from django.shortcuts import render
from django.views import generic
from .models import School
from .forms import SchoolForm


class SchoolCreateView(generic.CreateView):
    model = School
    form_class = SchoolForm
    template_name = 'school.html'


