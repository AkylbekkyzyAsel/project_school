from django.shortcuts import render
from django.views import generic
from .models import Course
from .forms import CourseForm

class CourseCreateView(generic.CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course.html'


