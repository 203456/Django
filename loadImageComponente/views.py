from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os.path
from pathlib import Path

# importaciones de modelos agregados
from loadImageComponente.models import imgField

# importaciones de serializadores
from loadImageComponente.serializer import imgSerializer

# Create your views here.

class imageView(APIView):
    def get(self, request, format=None):
        queryset = imgField.objects.all()
        serializer = imgSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "No hay imagen que subir")
        archivos = request.data['url_img']
        name, formato = os.path.splitext(archivos.name)
        request.data['name_img'] = name
        request.data['format_img'] = formato
        serializer = imgSerializer(data=request.data)

       
        if serializer.is_valid():
            validated_data = serializer.validated_data
            img = imgField(**validated_data)
            img.save()
            serializer_response = imgSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class ImageTableDetail(APIView):
    def get_object(self, pk):
        try:
            return imgField.objects.get(pk = pk)
        except imgField.DoesNotExist:
            return 0

    def get(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = imgSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay imagen", status = status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        archivos = request.data['url_img']

        name, formato = os.path.splitext(archivos.name)
        request.data['name_img'] = name
        request.data['format_img'] = formato
        serializer = imgSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        img = self.get_object(pk)
        if img != 0:
            img.delete()
            return Response( "imagen eliminada", status=status.HTTP_204_NO_CONTENT)
        return Response("Imagen no encontrada",status = status.HTTP_400_BAD_REQUEST) 