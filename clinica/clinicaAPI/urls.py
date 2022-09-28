
from django.urls import path
from . import views

urlpatterns = [
    path('newRegistro', views.newRegistro, name='newRegistro'),
    path('newPersona', views.newPersona, name='newPersona'),
    path('newPacien', views.newPacien, name='newPacien'),    
    path('newSignoVital', views.newSignoVital, name='newSignoVital'),    
    path('newMedico', views.newMedico, name='newMedico'),
    path('newFamiliar', views.newFamiliar, name='newFamiliar'),
    path('newEnfermero', views.newEnfermero, name='newEnfermero'),
    path('getAllPacientes', views.getAllPacientes, name='getAllPacientes'),
    path('getOnePaciente/<int:id>', views.getOnePaciente, name='getOnePaciente')
             
]