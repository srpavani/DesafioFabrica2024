from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import NutriModel
from .serializers import NutriSerializer
import requests

class NutriViewSet(ModelViewSet):
    queryset = NutriModel.objects.all()
    serializer_class = NutriSerializer

    def create(self, request, *args, **kwargs):
        nome = request.data.get('name', '')
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(nome)
        try: 
            requisicao = requests.get(api_url, headers={'X-Api-Key': 'HKiH5ZTgzjsCrA+QnCvkkQ==4xOj4GY24Aj7D8mU'})
            json = requisicao.json()
            if requisicao.status_code == 200 and json:
                item = json[0]
                nome = item.get('name', '')
                caloria = item.get('calories', '')
                proteina = item.get('protein_g', '')
                carboidrato = item.get('carbohydrates_total_g', '')
                acucar = item.get('sugar_g', '')

                dados_recebido = {
                    "nome": nome,
                    "caloria": caloria,
                    "proteina": proteina,
                    "carboidrato": carboidrato,
                    "acucar": acucar
                }
                serializer = NutriSerializer(data=dados_recebido)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "nao encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e: 
            print("error:", str(e))
            return Response({"error": "Erro interno do servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

