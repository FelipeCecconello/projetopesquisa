from django.contrib import admin
from .models import Professor, Aluno, ProjetoPesquisa, Atividade, Relatorio

admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(ProjetoPesquisa)
admin.site.register(Atividade)
admin.site.register(Relatorio)
