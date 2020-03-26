# from validate_docbr import CPF
from cpf_cnpj import Documento

# cpf = CPF() #instânciando

# print(cpf.validate("012.345.678-90"))


# cpf = Cpf("15316264754")

# print(cpf)

# exemplo_cnpj = "35379838000112"
# documento = CpfCnpj(exemplo_cnpj,'cnpj')
# print(documento)

# exemplo_cpf = "32007832062"
# documento = CpfCnpj(exemplo_cpf,'cpf')
# print(documento)

exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

exemplo_cpf = "32007832062"
documento = Documento.cria_documento(exemplo_cpf)
print(documento)
