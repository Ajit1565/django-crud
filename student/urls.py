from django.urls import  path
from . import views


urlpatterns=[
   path('home',views.home(),name='home'),
   path('add_student',views.add_students(),name='add_students'),

]