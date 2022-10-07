from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from teachers.forms import CreateTeacherForm, UpdateTeacherForm
from teachers.models import Teacher

from webargs.djangoparser import use_args
from webargs.fields import Str


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_teacher(request, args):
    teachers = Teacher.objects.all()

    if len(args) != 0 and args.get('first_name') or args.get('last_name'):
        teachers = teachers.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    return render(
        request=request,
        template_name='teacher/list.html',
        context={
            'title': 'List of teachers',
            'teachers': teachers,
        }
    )


def detail_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request=request,
                  template_name='teacher/detail.html',
                  context={
                      'title': 'Teacher\'s Details',
                      'teacher': teacher,
                  })


def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teacher:list'))

    return render(request, 'teacher/update.html', {'form': form})


def create_teacher(request):
    if request.method == 'GET':

        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teacher:list'))

    return render(request, 'teacher/create.html', {'form': form})


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teacher:list'))

    return render(request, 'teacher/delete.html', {'teacher': teacher})
