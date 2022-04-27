from django import forms
from .models import Group, Students, Lecture, Pass, List_Of_Control_Activities, \
    List_Of_Control_Activities_Value, Grade


class AddGroupStudent(forms.ModelForm):
    """ Форма создания группы учеников """

    class Meta:
        model = Group
        fields = "__all__"


class AddStudent(forms.ModelForm):
    """ Форма создания cтудентов """

    class Meta:
        model = Students
        fields = "__all__"


class AddLecture(forms.ModelForm):
    """ Форма создания Лекций """

    class Meta:
        model = Lecture
        fields = "__all__"


class AddGrade(forms.ModelForm):
    """ Форма создания оценок студентам """

    class Meta:
        model = Grade
        fields = "__all__"


class AddList(forms.ModelForm):
    """ Форма создания листа контрольных мероприятий """

    class Meta:
        model = List_Of_Control_Activities
        fields = "__all__"


class AddValue(forms.ModelForm):
    """ Форма создания содержимого в листе контрольных мероприятий """

    class Meta:
        model = List_Of_Control_Activities_Value
        fields = "__all__"


class AddPass(forms.ModelForm):
    """ Форма создания содержимого в листе контрольных мероприятий """

    class Meta:
        model = Pass
        fields = "__all__"
