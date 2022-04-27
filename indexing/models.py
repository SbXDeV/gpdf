from urllib import request

from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    """ Группа студентов """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Учитель')
    title = models.CharField(verbose_name='Название группы', max_length=1000)

    class Meta:
        verbose_name = 'Группы студентов'
        verbose_name_plural = 'Группа студентов'

    def __str__(self):
        return """ Название группы:  {}""".format(self.title)


class Lecture(models.Model):
    """ Лекция """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Учитель')
    title = models.CharField(verbose_name='Тема лекции', max_length=1000, help_text='Теория большого взрыва')
    date = models.DateField(verbose_name='Дата проведения')
    time = models.IntegerField(verbose_name='Длительность лекции', default=45)
    group = models.ManyToManyField(Group, verbose_name='Группа студентов', help_text='Это список доступных групп, '
                                                                                     'выберите у какой группы будет '
                                                                                     'лекция')

    class Meta:
        verbose_name = 'Лекции'
        verbose_name_plural = 'Лекций'

    def __str__(self):
        return """Лекция: {}""".format(self.title)


class Students(models.Model):
    """ Студенты """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Учитель')
    full_name = models.CharField(verbose_name='Фамилия Имя', max_length=1000, help_text='Савельев Максим')
    key = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')

    class Meta:
        verbose_name = 'Студента'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return """Студент: {}""".format(self.full_name)


class Grade(models.Model):
    """ Оценка """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Учитель')
    grades = models.IntegerField(verbose_name='Оценка', default=0)
    key = models.ForeignKey(Lecture, verbose_name='За лекцию', on_delete=models.CASCADE)
    key_to_student = models.ManyToManyField(Students, verbose_name='Студентам')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return """ Оценка: {}, за лекцию: {}""".format(self.grades, self.key.title)


class Pass(models.Model):
    """ Пропуски """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Учитель')
    key_to_student = models.ManyToManyField(Students, verbose_name='Студентам')
    date = models.DateField(verbose_name='Дата пропуска')

    class Meta:
        verbose_name = 'Пропуски'
        verbose_name_plural = 'Пропуски'

    def __str__(self):
        return """ Пропуск студента"""


class List_Of_Control_Activities(models.Model):
    """ Лист контрольных мероприятий """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Учитель')
    department = models.CharField(max_length=350, verbose_name='Кафедра')
    discipline = models.CharField(max_length=350, verbose_name='Дисциплина')
    course = models.IntegerField(verbose_name='Курс')
    semester = models.IntegerField(verbose_name='Семестр')
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    check_point_date_start = models.DateField(verbose_name='Контрольная точка #1')
    check_point_date_end = models.DateField(verbose_name='Контрольная точка #2')

    class Meta:
        verbose_name = ' Лист контрольных мероприятий'
        verbose_name_plural = ' Лист контрольных мероприятий'

    def __str__(self):
        return """  Лист контрольных мероприятий {}""".format(self.group.title)


class List_Of_Control_Activities_Value(models.Model):
    """ Лист контрольных мероприятий содержание"""
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Учитель')
    check_point = models.IntegerField(verbose_name='Контрольная точка')
    grade_service = models.CharField(verbose_name='Оценочное средство', max_length=350)
    form_holding = models.CharField(verbose_name='Форма проведения', max_length=350)
    order_holding = models.CharField(verbose_name='Порядок проведения', max_length=350)
    evaluation_scale = models.CharField(verbose_name='Шкала оценивания', max_length=350)
    evaluation_criteria = models.TextField(verbose_name='Критерии оценивания')
    value = models.ForeignKey(List_Of_Control_Activities, verbose_name='Содержание', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ' Лист контрольных мероприятий содержание'
        verbose_name_plural = ' Лист контрольных мероприятий содержание'

    def __str__(self):
        return """  Лист контрольных мероприятий """
