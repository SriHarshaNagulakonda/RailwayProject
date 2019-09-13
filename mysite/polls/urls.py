from django.urls import path

from . import views

app_name='polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('admin/',views.admin,name='admin'),
    path('admin/add_question/',views.add_question,name='add_question'),
    path('admin/insert_question/',views.insert_question,name='insert_question'),
    path('admin/edit_question',views.edit_question,name='edit_question'),
    path('admin/edit_question/<int:question_id>', views.change_question, name='change_question'),
    path('admin/update/<int:question_id>/',views.update,name='update')
]


'''
urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
]


'''

