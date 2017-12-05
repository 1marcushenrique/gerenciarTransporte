from django.shortcuts import render
from gerenciaTransp.models import *
# import para API
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from gerenciaTransp.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class SolicitarViewSet(viewsets.ModelViewSet):
    queryset = Solicitar.objects.all()
    serializer_class = SolicitarSerializer

class AtenderViewSet(viewsets.ModelViewSet):
    queryset = Atender.objects.all()
    serializer_class = AtenderSerializer

# Create your views here.
