from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import NutriModel
from .serializers import NutriSerializer
import requests

class NutriViewSet(ModelViewSet):
    queryset = NutriModel.objects.all()
    serializer_class = NutriSerializer

  
        


    def create(self, request):
        nome = request.data.get('name', '')
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(nome)
        requisicao = requests.get(api_url, headers={'X-Api-Key': 'HKiH5ZTgzjsCrA+QnCvkkQ==4xOj4GY24Aj7D8mU'})
        json = requisicao.json()
        print(json)
        if requisicao.status_code == 200:
            
            for item in json:
                nome = item.get('name', '')
                caloria = item.get('calories', '')
                proteina = item.get('protein_g', '')
                carboidrato = item.get('carbohydrates_total_g', '')
                acuca = item.get('sugar_g"', '')


            

            dados_recebido = {
                "nome": f"{nome}",
                "caloria": f"{caloria}",
                "proteina": f"{proteina}",
                "carboidrato": f"{carboidrato}",
                "acuca": f"{acuca}"
            }
            serializer = NutriSerializer(data=dados_recebido)
            if serializer.is_valid():
               # comida_pesquisada = NutriModel.objects
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Error:", requisicao.status_code, requisicao.text)
            return Response({"error": "nao encontrado"}, status=requisicao.status_code)

     