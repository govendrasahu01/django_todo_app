from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index_page"),
    path('adding',views.add_todo, name="add_todo"),
    path('marking <int:id>',views.marking, name="marking"),
    path('delete <int:id>',views.delete, name="delete"),
]
