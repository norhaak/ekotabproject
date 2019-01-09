from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Student, Step, Statuses, StudentForm
from django.urls import reverse_lazy
from django.utils.text import slugify


class StudentCreate(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'phone_number']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['first_name'])


class StudentUpdate(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('ekotab:list')


class StudentDelete(DeleteView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    success_url = reverse_lazy('ekotab:list')


class StepCreate(CreateView):
    model = Step
    fields = ['title']

class StepUpdate(UpdateView):
    model = Step
    fields = ['status', 'date_submitted', 'is_current_step']
    template_name_suffix = '_update_form'


class StepDelete(DeleteView):
    model = Step
    fields = ['title', 'status', 'date_added', 'is_current_step']
    success_url = reverse_lazy('ekotab:detail')







def student_list(request):
    student_list = Student.objects.all()
    return render(request, 'ekotab/student-list.html', {
        'student_list': student_list,
    })

def student_detail(request, student_slug):
    student = get_object_or_404(Student, slug=student_slug)
    step_list = student.steps.all()
    
    current_step = None
    query_result = student.steps.filter(is_current_step=True)
    if len(query_result) == 1:
        current_step = query_result[0]
    
    failed_step = None
    query_result = student.steps.filter(status__iexact=Statuses.FAILED.value)
    if len(query_result) == 1:
        failed_step = query_result[0]

    
    return render(request, 'ekotab/student-detail.html', {
        'student': student,
        'current_step': current_step,
        'failed_step': failed_step,
        'step_list': step_list
    })



