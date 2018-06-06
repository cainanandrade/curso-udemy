from django.conf.urls import url
from tarefas.views import nova_categoria, nova_tarefa, lista_categorias, lista_tarefas, delete_tarefa, editar_tarefa, delete_categoria, editar_categoria, search
from core.views import home

urlpatterns = [
    url(r'^nova-categoria/$', nova_categoria, name='nova_categoria'),
    url(r'^nova-tarefa/$', nova_tarefa, name='nova_tarefa'),
    url(r'^lista_tarefas/$', lista_tarefas, name='lista_tarefas'),
    url(r'^lista_categorias/$', lista_categorias, name='lista_categorias'),
    url(r'^buscas/$', search, name='search'),
    url(r'^delete-tarefa/(?P<id>[0-9]+)/$', delete_tarefa, name='delete_tarefa'),
    url(r'^delete-categoria/(?P<id>[0-9]+)/$', delete_categoria, name='delete_categoria'),
    url(r'^editar-tarefa/(?P<id>[0-9]+)/$', editar_tarefa, name='editar_tarefa'),
    url(r'^editar-categoria/(?P<id>[0-9]+)/$', editar_categoria, name='editar_categoria'),
]