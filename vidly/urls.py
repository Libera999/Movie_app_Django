from django.contrib import admin
from django.urls import path, include
from api.models import MovieResource
from . import views

movie_resource=MovieResource()

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')), #navigate to movies upon choosing movies as a path
    path('api/', include(movie_resource.urls))
]
