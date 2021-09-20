import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from school.models import Student

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        name = fake.name()
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(
                        random.randrange(10, 99),
                        random.randrange(100, 999),
                        random.randrange(100, 999),
                        random.randrange(0, 9))
        cellphone = "({}) 9{}-{}".format(
                        random.randrange(10, 21),
                        random.randrange(4000, 9999),
                        random.randrange(4000, 9999))
        p = Student(name=name, cpf=cpf, rg=rg, cellphone=cellphone, birth_date='2002-02-22')
        p.save()


criando_pessoas(50)