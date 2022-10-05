from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from groups.forms import CreateGroupForm, UpdateGroupForm
from groups.models import Group

from webargs.djangoparser import use_args
from webargs.fields import Str


@use_args(
    {
        'group_name': Str(required=False),
        'group_description': Str(required=False),
    },
    location='query'
)
def get_group(request, args):
    groups = Group.objects.all()

    if len(args) != 0 and args.get('group_name') or args.get('group_description'):
        groups = groups.filter(
            Q(group_name=args.get('group_name', '')) | Q(group_description=args.get('group_description', ''))
        )

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'title': 'List of Groups',
            'groups': groups
        }
    )


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


def update_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group:list'))

    return render(request, 'groups/update.html', {'form': form})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('group:list'))

    return render(request, 'groups/delete.html', {'group': group})
