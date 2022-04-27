from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, DetailView, ListView

from .forms import AddStudent, AddGroupStudent, AddLecture, AddGrade, AddValue, AddList, AddPass
from .models import *

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def index(request):
    lecture = Lecture.objects.filter(teacher__username=request.user)
    grade = Pass.objects.filter(teacher__username=request.user)
    context = {
        'lecture': lecture,
        'grade': grade
    }
    if request.user.is_authenticated:
        temp = 'profile/index.html'
    else:
        temp = 'account/login.html'
    return render(request, temp, context)


def profile(request):
    lecture = Lecture.objects.filter(teacher__username=request.user)
    grade = Pass.objects.filter(teacher__username=request.user)
    context = {
        'lecture': lecture,
        'grade': grade
    }
    if request.user.is_authenticated:
        temp = 'profile/index.html'
    else:
        temp = 'account/login.html'
    return render(request, temp, context)


# -------------------------------------------------------------------


class CreateGroup(CreateView):
    """ Форма создания группы студентов """
    template_name = 'profile/create_group.html'
    form_class = AddGroupStudent
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class CreateStudent(CreateView):
    """ Форма создания группы студентов """
    template_name = 'profile/create_student.html'
    form_class = AddStudent
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class CreateLecture(CreateView):
    """ Форма создания Лекции """
    template_name = 'profile/create_lecture.html'
    form_class = AddLecture
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class CreateGrade(CreateView):
    """ Форма создания оценок для студентов """
    template_name = 'profile/create_grade.html'
    form_class = AddGrade
    success_url = '/accounts/profile/table'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class CreateList(CreateView):
    """ Форма создания ЛККМ """
    template_name = 'profile/create_list.html'
    form_class = AddList
    success_url = '/accounts/profile/table-list'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class CreateValue(CreateView):
    """ Форма создания значений """
    template_name = 'profile/create_value.html'
    form_class = AddValue
    success_url = '/accounts/profile/table-list'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class CreatePass(CreateView):
    """ Форма создания значений """
    template_name = 'profile/create_pass.html'
    form_class = AddPass
    success_url = '/accounts/profile/table-pass'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


# -------------------------------------------------------------------
def table(request):
    tables = Grade.objects.filter(teacher__username=request.user)
    context = {
        'table': tables
    }
    if request.user.is_authenticated:
        temp = 'profile/table-data.html'
    else:
        temp = 'account/login.html'
    return render(request, temp, context)


def table_list(request):
    tables = List_Of_Control_Activities.objects.all().filter(teacher__username=request.user)
    context = {
        'rows': tables
    }
    if request.user.is_authenticated:
        temp = 'profile/table-data-list.html'
    else:
        temp = 'account/login.html'
    return render(request, temp, context)


def table_pass(request):
    tables = Pass.objects.filter(teacher__username=request.user)
    context = {
        'table': tables
    }
    if request.user.is_authenticated:
        temp = 'profile/table-data-pass.html'
    else:
        temp = 'account/login.html'
    return render(request, temp, context)


def table_delate(request, pk):
    tables = Grade.objects.get(id=pk)
    tables.delete()
    return redirect('/accounts/profile/table')


class Update_Table_View(UpdateView):
    model = Grade
    template_name = 'profile/create_grade.html'
    form_class = AddGrade
    success_url = '/accounts/profile/table'


class Update_Table_Pass_View(UpdateView):
    model = Pass
    template_name = 'profile/create_pass.html'
    form_class = AddPass
    success_url = '/accounts/profile/table-pass'


def table_delate_pass(request, pk):
    tables = Pass.objects.get(id=pk)
    tables.delete()
    return redirect('/accounts/profile/table-pass')


class Pdfer(ListView):
    model = List_Of_Control_Activities_Value
    template_name = 'pdf/index.html'
    context_object_name = 'serv'
