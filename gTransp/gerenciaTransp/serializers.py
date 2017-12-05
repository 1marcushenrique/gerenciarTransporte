from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from gerenciaTransp.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url', 'username', 'email', 'is_staff')


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    usuario=UserSerializer(many=False)
    class Meta:
        model = Funcionario
        fields = ('nome', 'fone', 'usuario')


    def create(self, dados):
      dados_user = dados.pop('usuario')
      u=User.objects.create(**dados_user)
      p=Funcionario.objects.create(usuario=u, **dados)
      return p

class VeiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Veiculo
        fields=('prefixo', 'marca', 'modelo', 'ano','placa')


class MotoristaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Motorista
        fields=('motorista', 'cnh', 'categoria')

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Departamento
        fields=('nome', 'setor')

class SolicitarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Solicitar
        fields= '__all__'

class AtenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Atender
        fields= '__all__'
