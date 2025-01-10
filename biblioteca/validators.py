from validate_docbr import CPF
import re

def validate_cpf(value):
    cpf = CPF()
    return cpf.validate(value)

def validate_email(value):
    regex = r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$'
    return re.match(regex, value) is not None

def validate_phone(value):
    regex = r'^\(\d{2}\)\s\d{4,5}-\d{4}$'
    return re.match(regex, value) is not None

def validate_name(value):
    regex = r'^[a-zA-Z\s]+$'
    return re.match(regex, value) is not None
#