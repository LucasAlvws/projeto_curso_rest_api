def validate_cpf(cpf):
        return (len(cpf) != 11 or not cpf.isnumeric())
            
def validate_nome(nome):
        nomes = nome.replace(" ", "")
        return not nomes.isalpha()

def validate_rg(rg):
        return (len(rg) != 9 and rg.isnumeric())

def validate_celular(celular):
        return len(celular) < 11
            