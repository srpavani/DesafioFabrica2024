from django.db import models

# Create your models here.

class NutriModel(models.Model):
    nome = models.CharField(verbose_name="nome", max_length=30)
    caloria = models.CharField(verbose_name="caloria", max_length=30, blank = True, null = True)
    proteina = models.CharField(verbose_name="proteina", max_length=30, blank = True)
    carboidrato = models.CharField(verbose_name="carboidrato", max_length=30, blank = True)
    acuca = models.CharField(verbose_name="acuca", max_length=30, blank = True)

    def __str__(self) -> str:
        return f"{self.nome} {self.caloria} {self.proteina} {self.carboidrato} {self.acuca}"
    






class RefeicaoModel(models.Model):
        nome= models.ForeignKey(NutriModel, on_delete=models.CASCADE)
        REFEICAO_CHOICES = (
        ("J", "Jantar"),
        ("C", "café"),
        ("N", "Nenhuma das opções"))
        tipo = models.CharField(verbose_name="tipo", max_length=1, choices=REFEICAO_CHOICES)
       
       
        
