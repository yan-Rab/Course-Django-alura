# Python
from datetime import date

# Third party
import re
from validate_docbr import CPF


def cpf_isvalid(cpf):
    cpf_validator = CPF()
    return cpf_validator.validate(cpf)


def name_isvalid(name):
    return name.isalpha()


def rg_isvalid(rg):
    return len(rg) == 9


def birth_date_isvalid(birth_date):
    return birth_date < date.today()


def cellphone_isvalid(cellphone):
    modelo = '\([0-9]{2}\) [0-9]{5}-[0-9]{4}'
    response = re.findall(modelo, cellphone)
    return response
