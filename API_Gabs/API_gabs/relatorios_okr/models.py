from django import db
from django.db import models

class TipoCliente(models.Model):
    tipo = (('V','VAREJO'), ('A','ATACADO'))
    categoria = models.CharField(max_length=50, choices=tipo)

    class Meta:
        managed = True
        db_table = "TipoCliente"

class Clientes(models.Model):
    sexo_choices = (('M', 'Masculino'),('F', 'Feminino'),('O', 'Outro'))
    #id = models.AutoField()
    nome = models.CharField(max_length=50, null=False)
    sexo = models.CharField(max_length=50, choices=sexo_choices, null=False)
    data_nasc = models.DateField()
    whatsapp = models.CharField(max_length=50)
    data_cadastro = models.DateField()
    tipo_cliente = models.ForeignKey(TipoCliente, models.CASCADE, db_column='categoria', related_name='id_tipo_cliente')

    class Meta:
        managed = True
        db_table = "Clientes"

        
#criar uma tabela que tenha como foreing keys o cliente.




##### NO SQLITE EXPLORER APARECE AS TABLES MAS NO DJANGO ADMIN NAO!