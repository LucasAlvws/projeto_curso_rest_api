import re
from validate_docbr import CPF
def validate_cpf(n_cpf):
        cpf = CPF()
        return cpf.validate(n_cpf)
            
def validate_nome(nome):
        nomes = nome.replace(" ", "")
        return not nomes.isalpha()

def validate_rg(rg):
        return (len(rg) != 9 and rg.isnumeric())

def validate_celular(celular):
        modelo = '[0-9]{2} [9]{1}[0-9]{4}-[0-9]{4}'
        resposta = re.findall(modelo, celular)
        return not resposta
            