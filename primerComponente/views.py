from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
#Importación de Modelos
from primerComponente.models import primerTabla
#Importación de Serializadors
from primerComponente.serializers import primerTablaSerializer
class primerTablaList(APIView):
    def get(self, request, format=None):
        queryset = primerTabla.objects.all()
        serializer = primerTablaSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data)