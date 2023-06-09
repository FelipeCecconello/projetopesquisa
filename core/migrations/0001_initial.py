# Generated by Django 4.2.1 on 2023-05-11 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjetoPesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('aprovado', models.BooleanField(default=False)),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('relatorio_pdf', models.FileField(upload_to='relatorios/')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.projetopesquisa')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.projetopesquisa')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=100)),
                ('projetos', models.ManyToManyField(blank=True, to='core.projetopesquisa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
