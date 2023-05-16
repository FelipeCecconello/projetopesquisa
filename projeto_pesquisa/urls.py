from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('criar_projeto/', views.criar_projeto, name='criar_projeto'),
    path('aprovar_projeto/<int:projeto_id>/', views.aprovar_projeto, name='aprovar_projeto'),
    path('executar_atividade/<int:atividade_id>/', views.executar_atividade, name='executar_atividade'),
    path('projeto/<int:projeto_id>/adicionar_relatorio/', views.adicionar_relatorio, name='adicionar_relatorio'),
    path('adicionar_atividade', views.adicionar_atividade, name='adicionar_atividade'),
    path('participar_projeto', views.participar_projeto, name='participar_projeto'),
    path('projeto/<int:projeto_id>/', views.pagina_projeto, name='pagina_projeto'),
    path('login_aluno/', views.login_aluno, name='login_aluno'),
    path('meus_projetos/', views.meus_projetos, name='meus_projetos'),
    path('meus_projetos_aluno/', views.meus_projetos_aluno, name='meus_projetos_aluno'),
    path('', views.login_professor, name='login'),
    path('relatorio/download/<int:relatorio_id>/', views.download_relatorio, name='download_relatorio'),
    path('projeto/<int:projeto_id>/adicionar_atividade/', views.adicionar_atividade, name='adicionar_atividade'),
]
