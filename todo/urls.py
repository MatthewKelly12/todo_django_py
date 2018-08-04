from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('add', views.addToDo, name='add'),
path('complete/<todo_id>', views.completeToDo, name='complete'),
path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
path('deleteall', views.deleteAll, name='deleteall')
]