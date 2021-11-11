from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    school = models.ForeignKey('school.School', on_delete=models.PROTECT)
    is_active = models.BooleanField()
    is_graduated = models.BooleanField(default=False)

class StudentCourse(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    courseId = models.ForeignKey('course.Course', on_delete=models.CASCADE)
