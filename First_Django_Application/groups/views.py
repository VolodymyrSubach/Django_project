from django.db.models import Q  # noqa
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from groups.forms import CreateGroupForm, GroupUpdateForm
from groups.models import Group

from students.models import Student

from webargs.djangoparser import use_args  # noqa
from webargs.fields import Str  # noqa


# def get_group(request):
#     groups = Group.objects.select_related('group')
#
#     filter_form = GroupFilterForm(data=request.GET, queryset=groups)
#
#     return render(
#         request=request,
#         template_name='groups/list.html',
#         context={
#             'title': 'List of Groups',
#             'groups': groups,
#             'filter_form': filter_form
#         }
#     )


class ListGroupView(ListView):
    model = Group
    template_name = 'groups/list.html'


def detail_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request=request,
                  template_name='groups/detail.html',
                  context={
                      'title': 'Group detail',
                      'group': group})


def create_group(request):
    if request.method == 'GET':

        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group:list'))

    return render(request, 'groups/create.html', {'form': form})


class CreateGroupView(CreateView):
    model = Group
    form_class = CreateGroupForm
    success_url = reverse_lazy('group:list')
    template_name = 'groups/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        group = form.save()
        students = form.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()

        return response


# def update_group(request, group_id):
#     group = get_object_or_404(Group, pk=group_id)
#     if request.method == 'GET':
#         form = GroupUpdateForm(instance=group)
#     elif request.method == 'POST':
#         form = GroupUpdateForm(request.POST, instance=group)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('group:list'))
#
#     return render(
#         request,
#         'groups/update.html',
#         {
#             'form': form,
#             'students': group.students.prefetch_related('headman_group')
#         }
#     )


class UpdateGroupView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('group:list')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            initial['headman_field'] = 0

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = int(form.cleaned_data['headman_field'])
        if pk:
            form.instance.headman = Student.objects.get(pk=pk)
        else:
            form.instance.headman = None
        form.save()

        return response


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('group:list'))

    return render(request, 'groups/delete.html', {'group': group})


class DeleteGroupView(DeleteView):
    pass
