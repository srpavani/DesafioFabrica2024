from rest_framework.serializers import ModelSerializer
from ..models import NutriModel


class NutriSerializer(ModelSerializer):
    class Meta:
        model = NutriModel
        fields = ["id", "nome", "caloria", "proteina", "carboidrato", "acuca"]



