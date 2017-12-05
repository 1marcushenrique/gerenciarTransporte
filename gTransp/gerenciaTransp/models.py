from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Departamento(models.Model):

    nome = models.CharField('nome ', max_length=100)
    setor = models.CharField('Setor ', max_length=100)


    def __str__(self):
        return str(self.nome + ' - Setor: '+ self.setor)

class Funcionario(models.Model):
    nome = models.CharField('Nome ', max_length=200)
    fone = models.CharField('FONE ', max_length=100)
    departamento = models.ForeignKey(Departamento)
    usuario=models.ForeignKey(User,  null=True, blank=False)



    def __str__(self):
        return str(self.nome)


class Veiculo(models.Model):
    prefixo = models.CharField('Prefixo ', max_length=20)
    marca = models.CharField('Marca ', max_length=50)
    modelo = models.CharField('Modelo ', max_length=50)
    ano = models.CharField('Ano ', max_length=10)
    placa = models.CharField('Placa ', max_length=8)

    def __str__(self):
        return str(self.modelo + ' - Prefixo: '+ self.prefixo )

class Motorista(models.Model):
    motorista = models.ForeignKey(Funcionario)
    cnh = models.CharField('CNH ', max_length=50)
    categoria = models.CharField('Categoria ', max_length=10)


    def __str__(self):
        return str(self.motorista.nome + ' - CNH: '+ self.cnh + ' - Categoria: '+ self.categoria)

class Solicitar(models.Model):

    departamento = models.ForeignKey(Departamento)
    dataH_ida = models.DateTimeField(blank=True, null=True)
    origem = models.CharField('Origem ', max_length=100)
    destino = models.CharField('Destino ', max_length=100)
    dataH_volta = models.DateTimeField(blank=True, null=True)
    motivo = models.CharField('Motivo ', max_length=100)
    funcionarios = models.ManyToManyField(Funcionario, max_length=100)


    def __str__(self):
        return str(self.departamento.nome  + ' - Origem: '+ self.origem + ' - Destino: '+ self.destino + ' - Motivo: '+ self.motivo)

class Atender(models.Model):
    dataH_liberacao = models.DateTimeField(blank=True, null=True)
    socilitacao = models.OneToOneField(Solicitar)
    veiculo = models.ForeignKey(Veiculo)
    motorista = models.ForeignKey(Motorista)
    funcionario = models.ForeignKey(Funcionario)
    situacao= models.BooleanField("Solicitação atendida?",default=False)


    def __str__(self):
        return str(self.socilitacao.departamento.nome  + ' - Veículo: '+ self.veiculo.prefixo + ' - Motorista: '+ self.motorista.motorista.nome + ' - FuncionarioDept.: '+ self.funcionario.departamento.nome)

# Create your models here.
