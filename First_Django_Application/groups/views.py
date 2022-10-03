from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token

from groups.forms import UpdateGroupForm
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
    group = Group.objects.get(pk=group_id)
    return render(request=request,
                  template_name='groups/detail.html',
                  context={
                      'title': 'Group detail',
                      'group': group})


def update_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
            {form.as_table()}
            </table>
            <input type="submit" value="Submit">
        </form>'''

    return HttpResponse(html_form)
