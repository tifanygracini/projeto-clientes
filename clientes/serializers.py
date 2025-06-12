from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido."})
    
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números neste campo."})
        
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 dígitos."})
        
        if validate_celular(data['celular']):
            raise serializers.ValidationError({'celular':"O celular deve ter 11 dígitos."})
        
        return data
    