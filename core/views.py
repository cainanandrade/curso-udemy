from django.shortcuts import render
#from tarefas.models import Tarefa

# Create your views here.

def home(request):
    #tarefa = Tarefa.objects.all() #SELECT * FROM Tarefa;
    return render(request, 'core/home.html')
