from django.urls import path
from . import views # import views from current directory

urlpatterns = [
   path('',views.index, name = 'index') #home page brings us to index and it will have a name of index
]
