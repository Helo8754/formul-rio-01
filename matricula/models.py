from django.db import models

LISTA_SEXO = [
    ('masculino', 'masculino'),
    ('feminino', 'feminino'),
]

# Create your models here.
class Alunos (models.Model):
    nome = models.CharField(max_length=150)
    endereço = models.CharField(max_length=150)
    email = models.EmailField()
    curso= models.CharField(max_length=100)
    sexo = models.CharField(max_length=100, choices=LISTA_SEXO)

    def __str__(self):
        return self.nome
        
