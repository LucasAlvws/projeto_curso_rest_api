from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate_cpf(self, cpf):
        if len(cpf) != 11 and cpf.isnumeric():
            raise serializers.ValidationError("O CPF deve ter 11 dígitos")
        return cpf
    def validate_nome(self,nome):
        if not nome.isalpha():
            raise serializers.ValidationError("O nome não pode conter números")
        return nome
    def validate_rg(self,rg):
        if len(rg) != 9 and rg.isnumeric():
            raise serializers.ValidationError("O CPF deve ter 9 dígitos")
        return rg