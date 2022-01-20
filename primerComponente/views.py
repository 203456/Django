from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
#Importación de Modelos
from primerComponente.models import primerTabla
#Importación de Serializadors
from primerComponente.serializers import primerTablaserielizer
class primerTablaList(APIView):
    def get(self, reques, format=None):
        queryset-primerTabla.objects.all()
        serializer = primerTablaserielizer(queryset, many=True, context = {'request': request})
        return Response.serializer.data