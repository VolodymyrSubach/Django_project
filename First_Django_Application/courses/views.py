from courses.forms import CourseFilterForm, CreateCourseForm, UpdateCourseForm
from courses.models import Course

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def get_course(request):
    courses = Course.objects.select_related('group')

    filter_form = CourseFilterForm(data=request.GET, queryset=courses)

    return render(
        request=request,
        template_name='courses/list.html',
        context={'courses': courses, 'filter_form': filter_form}
    )


def detail_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    return render(request=request, template_name='courses/detail.html', context={'course': course})


def create_course(request):
    if request.method == 'GET':

        form = CreateCourseForm()
    elif request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('course:list'))

    return render(request, 'courses/create.html', {'form': form})


def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'GET':
        form = UpdateCourseForm(instance=course)
    elif request.method == 'POST':
        form = UpdateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('course:list'))

    return render(request, 'courses/update.html', {'form': form, 'course': course})


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('course:list'))

    return render(request, 'courses/delete.html', {'course': course})
