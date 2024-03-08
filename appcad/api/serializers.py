from rest_framework.serializers import ModelSerializer
from ..models import NutriModel
from ..models import RefeicaoModel


class NutriSerializer(ModelSerializer):
    class Meta:
        model = NutriModel
        fields = ["id", "nome", "caloria", "proteina", "carboidrato", "acuca"]


class RefeicaoSerializer(ModelSerializer):
    class Meta:
        model = RefeicaoModel
        fields = ["id", "nome", "caloria", "proteina", "carboidrato", "acuca"]

