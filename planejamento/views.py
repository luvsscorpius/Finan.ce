from django.shortcuts import render
from perfil.models import Categoria
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import calcula_total
from extrato.models import Valores

def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor = json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    categoria.save()
    return JsonResponse({'Status': 'Sucesso'})

def ver_planejamento(request):
    categorias = Categoria.objects.all()
    valores = Valores.objects.all().filter(tipo='S')
    total = calcula_total(valores, 'valor')
    total_percentual = int(total / 100)
    print(total_percentual)
    return render(request, 'ver_planejamento.html', {'categorias': categorias, 'total_percentual': total_percentual})