from django.shortcuts import render, get_object_or_404
from .models import Student, Step, Statuses


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



