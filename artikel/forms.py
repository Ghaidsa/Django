from django import forms  
from django_ckeditor_5.widgets import CKEditor5Widget
from artikel.models import Kategori, ArtikelBlog

class KategoriForms(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ('nama',)
        widgets = {
            "nama" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'required' : 'True' 
                }),     
        }

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = ArtikelBlog
        fields = ('kategori','judul','isi','gambar','status')
        widgets = {
            "kategori" : forms.Select(
                attrs={
                    'class' : 'form-control',
                    'required' : 'True' 
                }),

            "judul" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'required' : 'True' 
                }), 
            "isi" : CKEditor5Widget(
                config_name='default',
                attrs={
                    'class' : 'form-control mb-3 django_ckeditor_5',
                }),     
            "gambar" : forms.FileInput(
                attrs={
                    'class' : 'form-ClearableFileInput',
                    'required' : 'True' 
                }), 
             "status" : forms.Select(
                attrs={
                    'class' : 'form-control',
                    'required' : 'True' 
                }),          
        }         
                
        