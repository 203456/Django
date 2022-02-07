from http.client import OK
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#Importación Json
import json


# Create your views here.
#Importación de Modelos

from primerComponente.models import primerTabla
#Importación de Serializadors

from primerComponente.serializers import primerTablaSerializer







class primerTablaList(APIView):
    
    def response_Custom(self, message, data, status  ): 
        responseCustom = {"messages": "success", "payload": data, "status": status}
        responsJ=json.dumps(responseCustom)
        responseOK = json.loads(responsJ)
        return responseOK

    def get(self, request, format=None):
        queryset = primerTabla.objects.all()
        serializer = primerTablaSerializer(queryset,many=True,context={'request':request})
        responseOK = self.response_Custom("message", serializer.data, status.HTTP_200_OK)
        return Response(responseOK)

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

            
    def delete(self, request, pk, format=None):
        objetive = self.get_object(pk)
        if objetive!="No existe":
            objetive.delete()
            return Response("Usuario eliminado",  status = status.HTTP_200_OK)
        else:
            return Response("Usuario no encontrado", status = status.HTTP_400_BAD_REQUEST)