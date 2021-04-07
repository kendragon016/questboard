from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home', home_view, name='home'),
    path('create', create_view, name='create'),
    path('list', list_view, name='list'),
    path('edit/<int:pk>', edit_view, name='edit'),
    path('add', add_view, name='add'),
    path('board/teacher/<int:pk>', board_view, name='board'),
]
