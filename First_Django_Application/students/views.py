from django.db.models import Q  # noqa
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt  # noqa
from django.views.generic import UpdateView

from core.views import CustomUpdateBaseView # noqa

from students.forms import CreateStudentForm, StudentFilterForm
from students.forms import UpdateStudentForm
from students.models import Student


# @use_args(
#     {
#         'first_name': Str(required=False),
#         'last_name': Str(required=False),
#     },
#     location='query'
# )
def get_students(request):
    students = Student.objects.select_related('group')

    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    # if len(args) != 0 and args.get('first_name') or args.get('last_name'):
    #     students = students.filter(
    #         Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
    #     )

    return render(
        request=request,
        template_name='students/list.html',
        context={
            # 'title': 'List of students',
            # 'students': students,
            'filter_form': filter_form
        }
    )


def detail_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})


# @csrf_exempt
def create_student(request):
    if request.method == 'GET':

        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/create.html', {'form': form})


# def update_student(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#
#     if request.method == 'POST':
#         form = UpdateStudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#
#     form = UpdateStudentForm(instance=student)
#
#     return render(request, 'students/update.html', {'form': form})


# class CustomUpdateStudentView(CustomUpdateBaseView):
#     model = Student
#     form_class = UpdateStudentForm
#     success_url = 'students:list'
#     template_name = 'students/update.html'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': student})
