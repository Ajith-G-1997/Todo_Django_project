from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add-task/',views.add_task,name='add_task'),
    path('mark_as_done/<int:task_id>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:task_id>/', views.mark_as_undone, name='mark_as_undone'),
    path('update_task/<int:update_id>/', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

   
]