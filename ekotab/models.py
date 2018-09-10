from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.utils.text import slugify
import datetime
from .utils import ChoiceEnum

STEP_STATUSES = (
    ('O', 'Ongoing'),
    ('S', 'Submitted'),
    ('F', 'Failed'),
    ('P', 'Passed')
)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def getCurrentStep(self):
        current_step = None
        query_result = self.steps.filter(is_current_step=True)
        if len(query_result) == 1:
            current_step = query_result[0]
        return current_step


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class Statuses(ChoiceEnum):
        ONGOING = 'Ongoing'
        SUBMITTED = 'Submitted'
        FAILED = 'Failed'
        PASSED = 'Passed'

class Step(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='steps')
    title = models.CharField(max_length=20)
    status = models.CharField(max_length=9, choices=Statuses.choices(), default=Statuses.ONGOING)
    date_added = models.DateField('date added', default=datetime.date.today)
    date_submitted = models.DateField('date submitted', blank=True, null=True)
    is_current_step = models.BooleanField(default=False)

    def __str__(self):
        return "Step {} for student: {}".format(self.title, self.student)
