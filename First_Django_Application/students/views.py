from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from django.views.generic import UpdateView

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
# def get_students(request):
#     students = Student.objects.select_related('group')
#
#     filter_form = StudentFilterForm(data=request.GET, queryset=students)
#
#     # if len(args) != 0 and args.get('first_name') or args.get('last_name'):
#     #     students = students.filter(
#     #         Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
#     #     )
#
#     return render(
#         request=request,
#         template_name='students/list.html',
#         context={
#             # 'title': 'List of students',
#             # 'students': students,
#             'filter_form': filter_form
#         }
#     )


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'
    paginate_by = 12

    def get_filter(self):
        students = Student.objects.select_related('group')
        filter_form = StudentFilterForm(data=self.request.GET, queryset=students)

        return filter_form

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_filter().form

        return context


# @login_required
# def detail_student(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#     return render(request, 'students/detail.html', {'student': student})


class DetailStudentView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'students/detail.html'


# @login_required
# def create_student(request):
#     if request.method == 'GET':
#
#         form = CreateStudentForm()
#     elif request.method == 'POST':
#         form = CreateStudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#
#     return render(request, 'students/create.html', {'form': form})


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = CreateStudentForm
    template_name = 'students/create.html'
    success_url = reverse_lazy('students:list')

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     student = form.save()
    #
    #     return response


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


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


# @login_required
# def delete_student(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('students:list'))
#
#     return render(request, 'students/delete.html', {'student': student})


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:list')
