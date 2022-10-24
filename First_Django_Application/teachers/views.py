from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from teachers.forms import CreateTeacherForm, UpdateTeacherForm
from teachers.models import Teacher


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teacher/list.html'


class DetailTeacherView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teacher/detail.html'


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    template_name = 'teacher/update.html'
    success_url = reverse_lazy('teacher:list')

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['subject_name'] = self.object.subject_name
        except AttributeError:
            initial['subject_name'] = 0

        return initial


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = CreateTeacherForm
    template_name = 'teacher/create.html'
    success_url = reverse_lazy('teacher:list')


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teacher/delete.html'
    success_url = reverse_lazy('teacher:list')
