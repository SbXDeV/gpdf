from django.urls import path
from .views import *
app_name = 'Index'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/create-group', CreateGroup.as_view(), name='group'),
    path('accounts/profile/create-student', CreateStudent.as_view(), name='student'),
    path('accounts/profile/create-lecture', CreateLecture.as_view(), name='Lecture'),
    path('accounts/profile/create-grade', CreateGrade.as_view(), name='grade'),
    path('accounts/profile/create-list', CreateList.as_view(), name='list'),
    path('accounts/profile/create-value', CreateValue.as_view(), name='value'),
    path('accounts/profile/create-pass', CreatePass.as_view(), name='pass'),
    # Таблицы
    path('accounts/profile/table', table, name='table'),
    path('accounts/profile/table-list', table_list, name='table-list'),
    path('accounts/profile/table/<int:pk>', table_delate, name='table-delete'),
    path('accounts/profile/table/<int:pk>/update', Update_Table_View.as_view(), name='table-update'),
    path('accounts/profile/pdf/', Pdfer.as_view(), name='pdf_gen')

]