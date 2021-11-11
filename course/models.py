from django.db import models
from django.core.validators import MaxValueValidator

class Course(models.Model):

    name = models.CharField(max_length=255)
    school = models.ForeignKey('school.School', on_delete=models.PROTECT)
    is_active = models.BooleanField()
    price = models.DecimalField(decimal_places=2, max_digits=2)
    duration = models.DurationField()
    max_students = models.PositiveIntegerField(validators=[MaxValueValidator(20)])

