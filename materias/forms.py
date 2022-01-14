from django.db.models import fields
#from sauv.materias.views import materias_lista
from django import forms
from django.forms import widgets
from materias.models import Programa,Materia,Archivosmaterias

class programaForm(forms.ModelForm):
    class Meta:
        model=Programa

        fields=[
            'nombrePrograma',
            'numPeriodos',
        ]
        labels={
             'nombrePrograma':'Nombre del programa',
             'numPeriodos':'Numero de periodos',

        }
        widgets={
             'nombrePrograma':forms.TextInput(attrs={'class':'form-control'}),
             'numPeriodos':forms.TextInput(attrs={'class':'form-control'}),
        }


class materiaForm(forms.ModelForm):
            class Meta:
                model=Materia

                fields=[
                    'idPrograma',
                    'nombreMateria',
                    'numPeriodo',
                ]
                labels={
                    'idPrograma':'Programa Educativo',
                    'nombreMateria':'Nombre de la materia',
                    'numPeriodo':'Periodo correspondiente',
                }
                widgets={
                    'idPrograma':forms.Select,
                    'nombreMateria':forms.TextInput(attrs={'class':'form-control'}),
                    'numPeriodo':forms.TextInput(attrs={'class':'form-control'}),
                }        

class uploadArchivos(forms.ModelForm):
    class Meta:
        model=Archivosmaterias
        fields=['materia','presentacion','bloque1','bloque2','bloque3','bloque4','bloque5','bloque6',
                'bloque7','bloque8','bloque9','bloque10','foroact1','foroact2','foroact3','foroact4',
                'foroact5','foroact6','foroact7','foroact8','foroact9','foroact10','examen1','examen2','examen3',
                ]
        labels={
            'materia':'Nombre de la materia',
            'presentacion':'Presentacion de la materia',
            'bloque1':'Contenido del bloque 1',
            'bloque2':'Contenido del bloque 2',
            'bloque3':'Contenido del bloque 3',
            'bloque4':'Contenido del bloque 4',
            'bloque5':'Contenido del bloque 5',
            'bloque6':'Contenido del bloque 6',
            'bloque7':'Contenido del bloque 7',
            'bloque8':'Contenido del bloque 8',
            'bloque9':'Contenido del bloque 9',
            'bloque10':'Contenido del bloque 10',
            'foroact1':'Foros y actividades del bloque 1',
            'foroact2':'Foros y actividades del bloque 2',
            'foroact3':'Foros y actividades del bloque 3',
            'foroact4':'Foros y actividades del bloque 4',
            'foroact5':'Foros y actividades del bloque 5',
            'foroact6':'Foros y actividades del bloque 6',
            'foroact7':'Foros y actividades del bloque 7',
            'foroact8':'Foros y actividades del bloque 8',
            'foroact9':'Foros y actividades del bloque 9',
            'foroact10':'Foros y actividades del bloque 10',
            'examen1':'Formato de examen parcial 1',
            'examen2':'Formato de examen parcial 2',
            'examen3':'Formato de examen parcial 3',
        }      
