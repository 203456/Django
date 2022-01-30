from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

    def post(self, request, format=None): 
        serializer = primerTablaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)   

class primerTablaDetail(APIView):
    def get_object(self, pk):
        try:
            return primerTabla.objects.get(pk = pk)  
        except primerTabla.DoesNotExist:   
            return 0
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = primerTablaSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)    

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = primerTablaSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)   

            
