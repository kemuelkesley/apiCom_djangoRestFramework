from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Número de CPF invalido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Nome não pode conter números"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "RG deve ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "Celular deve seguir o padrão 11 91234-1234"})
        return data
     
