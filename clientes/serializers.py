from rest_framework import serializers
from clientes.models import Cliente
from .validators import validate_cpf, validate_nome,validate_rg, validate_celular

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if validate_cpf(data['cpf']):
            raise serializers.ValidationError({"cpf":"O CPF deve ter 11 dígitos"})
        if validate_nome(data['nome']):
            raise serializers.ValidationError({"nome":"O nome não pode conter números"})
        if validate_rg(data['rg']):
            raise serializers.ValidationError({"rg":"O RG deve ter 9 dígitos"})
        if validate_celular(data['celular']):
            raise serializers.ValidationError({"celular":"O número não está correto"})
        
        return data
    
    
    
            