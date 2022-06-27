from django.urls import path
from . import views # import views from current directory

urlpatterns = [
   path('',views.index, name = 'movies_index'), #home page brings us to index and it will have a name of index
   path('<movie_id>', views.detail,name='movies_detail')
]
