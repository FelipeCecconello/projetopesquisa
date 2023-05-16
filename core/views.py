from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Professor, ProjetoPesquisa, Atividade, Relatorio, Aluno
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse

def criar_projeto(request):
    if request.method == 'POST':
        professor = Professor.objects.get(id=request.user.id)
        titulo = request.POST['titulo']
        projeto = ProjetoPesquisa.objects.create(professor=professor, titulo=titulo)
        # Lógica adicional, se necessário
        return redirect('pagina_projeto', {'projeto': projeto})  # Redirecionar para a página de projetos
    return render(request, 'criar_projeto.html')

def aprovar_projeto(request, projeto_id):
    projeto = ProjetoPesquisa.objects.get(id=projeto_id)
    projeto.aprovado = True
    projeto.save()
    # Lógica adicional, se necessário
    return redirect('pagina_projeto', {'projeto': projeto})  # Redirecionar para a página de projetos

def adicionar_atividade(request, projeto_id):
    if request.method == 'POST':
        projeto = ProjetoPesquisa.objects.get(id=projeto_id)
        descricao = request.POST['descricao']
        atividade = Atividade.objects.create(projeto=projeto, descricao=descricao)
        # Lógica adicional, se necessário
        return redirect('pagina_projeto', projeto_id=projeto_id)  # Redirecionar para a página de projetos
    return render(request, 'adicionar_atividade.html')

def adicionar_relatorio(request, projeto_id):
    if request.method == 'POST':
        projeto = ProjetoPesquisa.objects.get(id=projeto_id)
        descricao = request.POST['descricao']
        titulo = request.POST['titulo']
        relatorio_pdf = request.FILES['relatorio_pdf']
        relatorio = Relatorio.objects.create(projeto=projeto, descricao=descricao, relatorio_pdf=relatorio_pdf, titulo=titulo)
        # Lógica adicional, se necessário
        return redirect('pagina_projeto', projeto_id=projeto_id)  # Redirecionar para a página de projetos
    return render(request, 'adicionar_relatorio.html')

def participar_projeto(request, projeto_id):
    if request.method == 'POST':
        aluno = Aluno.objects.get(id=request.user.id)
        projeto = ProjetoPesquisa.objects.get(id=projeto_id)
        projeto.alunos.add(aluno)
        # Lógica adicional, se necessário
        return redirect('pagina_projeto', {'projeto': projeto})  # Redirecionar para a página de projetos
    return render(request, 'participar_projeto.html')

def executar_atividade(request, atividade_id):
    atividade = Atividade.objects.get(id=atividade_id)
    # Lógica para executar a atividade
    # Lógica adicional, se necess�rio
    return redirect('pagina_projeto')  # Redirecionar para a página de projetos

def pagina_projeto(request, projeto_id):
    projeto = get_object_or_404(ProjetoPesquisa, id=projeto_id)
    relatorios = Relatorio.objects.filter(projeto=projeto_id)
    atividades = Atividade.objects.filter(projeto=projeto_id)
    return render(request, 'pagina_projeto.html', {'projeto': projeto,'relatorios': relatorios, 'atividades' : atividades})

def login_professor(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('meus_projetos')
    
    return render(request, 'index.html')

def login_aluno(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('meus_projetos_aluno')
    
    return render(request, 'login_aluno.html')

@login_required
def meus_projetos(request):
    projetos = ProjetoPesquisa.objects.filter(professor=request.user.professor)
    return render(request, 'meus_projetos.html', {'projetos': projetos})

@login_required
def meus_projetos_aluno(request):
    aluno = request.user.aluno
    atividades = Atividade.objects.filter(projeto=request.user.aluno.projeto)
    return render(request, 'meus_projetos_aluno.html', {'aluno': aluno, 'atividades':atividades})

def download_relatorio(request, relatorio_id):
    relatorio = Relatorio.objects.get(id=relatorio_id)

    # Código para obter o caminho do arquivo do relatório
    relatorio_path = relatorio.relatorio_pdf.path

    # Abra o arquivo para leitura binária
    with open(relatorio_path, 'rb') as relatorio_file:
        response = HttpResponse(relatorio_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=relatorio.pdf'
        return response
    
