from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import CategoriaForm, TarefaForm
from .models import Categoria, Tarefa
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def nova_categoria(request):
    if request.method=='POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('tarefas:lista_categorias')
        else:
            print(form.errors)

    else:
        form = CategoriaForm()

    return render(request, 'tarefas/nova_categoria.html', {'form': form})

@login_required
def delete_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id, user=request.user).delete()
    return redirect('tarefas:lista_categorias')

@login_required
def nova_tarefa(request):
    if request.method=='POST':
        form = TarefaForm(user=request.user, data=request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('tarefas:lista_tarefas')
        else:
            print(form.errors)

    else:
        form = TarefaForm(user=request.user)

    return render(request, 'tarefas/nova_tarefa.html', {'form': form})

@login_required
def lista_categorias(request):
    categoria = Categoria.objects.filter(user=request.user)
    return render(request, 'tarefas/lista_categorias.html', {'categoria':categoria})

@login_required
def lista_tarefas(request):
    tarefa = Tarefa.objects.filter(user=request.user, status='')
    return render(request, 'tarefas/lista_tarefas.html', {'tarefa': tarefa})

@login_required
def delete_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id, user=request.user).delete()
    return redirect('tarefas:lista_tarefas')

@login_required
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id, user=request.user)
    if request.method=='POST':
        form = TarefaForm(user=request.user, data=request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefas:lista_tarefas')
        else:
            print(form.errors)

    else:
        form = TarefaForm(user=request.user, instance=tarefa)

    return render(request, 'tarefas/nova_tarefa.html', {'form': form})

@login_required
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id, user=request.user)
    if request.method=='POST':
        form = CategoriaForm(user=request.user, data=request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('tarefas:lista_categorias')
        else:
            print(form.errors)
    else:
        form = CategoriaForm(user=request.user, instance=categoria)
    return render(request, 'tarefas/nova_categoria.html', {'form':form})

@login_required
def search(request):
    q=request.GET.get('search')
    if q is not None:
        result = Tarefa.objects.search(q, request.user)
    return render(request, 'tarefas/pagina_resultado.html', {'result':result})