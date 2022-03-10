# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from django.contrib.auth.models import User
import os.path


# importaciones de modelos agregados
from Profile.models import Profiles

# importaciones de serializadores
from Profile.serializer import ProfileSerializer


class UserView(APIView):
    def get_objectUser(self, idUser):
        try:
            return User.objects.get(pk = idUser)
        except User.DoesNotExist:
            return 404
    
    def post(self, request):
            archivos = request.data['url_img']
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                img = Profiles(**validated_data)
                img.save()
                serializer_response = ProfileSerializer(img)
                return Response(serializer_response.data, status=status.HTTP_201_CREATED)
            return Response("Este usuario tiene un perfil existente")
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return Profiles.objects.get(id_user = pk)
        except Profiles.DoesNotExist:
            return 404
    def res_custom(self, user, data, status):
        response = {
            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "username" : user[0]['username'],
            "email" : user[0]['email'],
            "id_user" : data.get('id_user'),
            "url_img" : data.get('url_img'),
        }
        return response;
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            idResponse = ProfileSerializer(idResponse)
            user = User.objects.filter(id=pk).values()
            responseOK = self.res_custom(user,idResponse.data,status.HTTP_200_OK)
            return Response(responseOK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        archivos = request.data['url_img']
        idResponse = self.get_object(pk)
        if(idResponse != 404):
            serializer = ProfileSerializer(idResponse)
            try:
                os.remove('assets/'+str(idResponse.url_img))
            except os.error:
                print("La imagen no existe")
            idResponse.url_img = archivos
            idResponse.save()
            return Response("Request exitoso",status.HTTP_201_CREATED)
        else:
            return Response("Request fallido")
    
    def delete(self, request, pk):
        profile = self.get_object(pk)
        if profile != 404:
            profile.url_img.delete(save=True)
            return Response("Imagen eliminada",status=status.HTTP_204_NO_CONTENT)
        return Response("Imagen no encontrada",status = status.HTTP_400_BAD_REQUEST)
class UserProfile(APIView):
    
    def res_custom(self, user, status):
        response = {
            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "username" : user[0]['username'],
            "email" : user[0]['email']
        }
        return response;
    
    def get(self, request, pk, format=None):
        idResponse = User.objects.filter(id=pk).values()
        if(idResponse != 404):
            responseData = self.res_custom(idResponse, status.HTTP_200_OK)
            return Response(responseData)
        return("Usuario no encontrado")
    
    def put(self, request, pk, format=None):
        data = request.data
        user = User.objects.filter(id = pk)
        user.update(username = data.get('username'))
        user.update(first_name = data.get('first_name'))
        user.update(last_name = data.get('last_name'))
        user.update(email = data.get('email'))
        user2 = User.objects.filter(id=pk).values()
        return Response(self.res_custom(user2, status.HTTP_200_OK))
    