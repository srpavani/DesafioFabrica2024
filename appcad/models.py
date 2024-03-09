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
    

        
       
        
