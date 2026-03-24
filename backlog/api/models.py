from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14, blank=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL_CHOICES = [
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    ]
    
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL_CHOICES, default='B')
    carga_horaria = models.PositiveIntegerField()

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    PERIODO_CHOICES = [
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    ]
    
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')
    periodo = models.CharField(max_length=1, choices=PERIODO_CHOICES, default='M')

    def __str__(self):
        return f'{self.estudante} - {self.curso}'