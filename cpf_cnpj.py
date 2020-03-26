from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos esta incorreta!!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!!!")

    def __str__(self):
        return self.format()

    def valida(self, documento):        
        validator = CPF()
        return validator.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!!!")

    def __str__(self):
        return self.format()

    def valida(self, documento):        
        validator = CNPJ()
        return validator.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

# class CpfCnpj:

#     def __init__(self, documento, tipo_documento):
#         self.tipo_documento = tipo_documento
#         documento = str(documento)
#         if self.tipo_documento == "cpf":
#             if self.cpf_eh_valido(documento):
#                 self.cpf = documento            
#             else:
#                 raise ValueError("CPF inválido!!")
#         elif self.tipo_documento == "cnpj":
#             if self.cnpj_eh_valido(documento):
#                 self.cnpj = documento            
#             else:
#                 raise ValueError("CNPJ inválido!!")
#         else:
#             raise ValueError("Documento inválido!!")

#     def __str__(self):
#         if self.tipo_documento == "cpf":
#             return self.format_cpf()
#         elif self.tipo_documento == "cnpj":
#             return self.format_cnpj()      
        
        
#     def cpf_eh_valido(self, cpf):
#         if len(cpf) == 11:
#             validator = CPF()
#             return validator.validate(cpf)
#         else:
#             raise ValueError("Quantidade de dígitos inválida!!")

#     def format_cpf(self):
#         # fatia_um = self.cpf[:3]
#         # fatia_dois = self.cpf[3:6]
#         # fatia_tres = self.cpf[6:9]
#         # fatia_quatro = self.cpf[9:]
#         # return ("{}.{}.{}-{}".format(fatia_um, fatia_dois, fatia_tres, fatia_quatro))
#         mascara = CPF()
#         return mascara.mask(self.cpf)

#     def cnpj_eh_valido(self, cnpj):
#         if len(cnpj) == 14:
#             validator = CNPJ()
#             return validator.validate(cnpj)
#         else:
#             raise ValueError("Quantidade de dígitos inválida!!")

#     def format_cnpj(self):        
#         mascara = CNPJ()
#         return mascara.mask(self.cnpj)