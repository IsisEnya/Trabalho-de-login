from django.contrib import admin
from .models import User, Profile, Post, Comment    
from contas.models import funcionario 

class User(admin.ModelAdmin):
    list_display = ('id', 'nome','cep', 'email')
    list_display_links = ('nome', 'cep','email')
    search_fields=('nome','id')

    admin.site.register(User,User)

