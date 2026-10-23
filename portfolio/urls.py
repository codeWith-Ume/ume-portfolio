from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('skills',views.skill,name='skill'),
    path('project',views.project,name='project'),
    path('resume',views.resume,name='resume'),
    path('contact',views.contact,name='contact')
]