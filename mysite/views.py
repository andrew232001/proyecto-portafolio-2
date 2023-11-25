from django.shortcuts import render

#debo borrar este codigo
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def tu_vista(request):
    # Tu lógica de vista aquí
    return HttpResponse("admin/")

# Create your views here.
