from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    # Outros campos para o professor

class ProjetoPesquisa(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    aprovado = models.BooleanField(default=False)
    inicio = models.DateField()
    fim = models.DateField()

class Atividade(models.Model):
    projeto = models.ForeignKey(ProjetoPesquisa, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)

class Relatorio(models.Model):
    projeto = models.ForeignKey(ProjetoPesquisa, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    relatorio_pdf = models.FileField(upload_to='relatorios/')

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projeto = models.ForeignKey(ProjetoPesquisa, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    # Outros campos para o aluno
