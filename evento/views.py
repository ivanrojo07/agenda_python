from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime
from .models import Evento
from .serializers import EventoSerializer
from django.http import Http404
# Create your views here.

@api_view(['POST'])
def eventUser(request):
    user_id = request.data.get('user_id')
    if user_id:
        try:
            eventos = Evento.objects.filter(usuario_id=user_id)
            serializer =EventoSerializer(eventos,many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'errors':{
            "user_id":"El campo user_id es obligatorio y en formato númerico"
        }}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'errors':{
            "user_id":"El campo user_id es obligatorio y en formato númerico"
        }}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def eventForDays(request):
    user_id = request.data.get('user_id')
    date = request.data.get('date')
    if user_id and date:
        try:
            date_time = datetime.strptime(date, '%Y-%m-%d')
            eventos = Evento.objects.filter(usuario_id=user_id).exclude(inicio__gte=datetime.today()).filter(inicio__gte=date_time)
            serializer = EventoSerializer(eventos,many=True)
            return Response(serializer.data)
        except(ValueError, Exception ) as e:
            print(e)
            if(isinstance(e,ValueError)):
                print("es value error")
                return Response({'errors':{"Formato incorrecto "+str(e)}}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'errors':{str(e)}}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'errors':{
            "user_id":"El campo user_id es obligatorio y en formato númerico",
            "date":"El campo date es obligatorio y en formato Y-m-d"
        }}, status=status.HTTP_400_BAD_REQUEST)
class ListEvento(APIView):

    def get_object(self,pk):
        try:
            return Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            raise Http404

    

    def get(self,request, pk=None, format=None):
        if(pk is None):
            eventos = Evento.objects.all()
            serializer = EventoSerializer(eventos,many=True)
            return Response(serializer.data)
        else:
            evento = self.get_object(pk)
            serializer = EventoSerializer(evento)
            return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        if('fecha_inicio' in data):
            data['inicio'] = datetime.strptime(data['fecha_inicio']+" "+(data['hora_inicio'] if 'hora_inicio' in data else "00:00:00"),"%Y-%m-%d %H:%M:%S")
        if('fecha_fin' in data):
            data['fin'] = datetime.strptime(data['fecha_fin']+" "+(data['hora_fin'] if 'hora_fin' in data else "00:00:00"),"%Y-%m-%d %H:%M:%S")
        if('fecha_recordatorio' in data):
            data['recordatorio'] = datetime.strptime(data['fecha_recordatorio']+" "+(data['hora_recordatorio'] if 'hora_recordatorio' in data else "00:00:00"),"%Y-%m-%d %H:%M:%S")
        serializer = EventoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk, format=None):
        data = request.data
        evento = self.get_object(pk)
        if('fecha_inicio' in data):
            data['inicio'] = datetime.strptime(data['fecha_inicio']+" "+(data['hora_inicio'] if 'hora_inicio' in data else "00:00:00"),"%Y-%m-%d %H:%M:%S")
        if('fecha_fin' in data):
            data['fin'] = datetime.strptime(data['fecha_fin']+" "+(data['hora_fin'] if 'hora_fin' in data else "00:00:00"),"%Y-%m-%d %H:%M:%S")
        if('fecha_recordatorio' in data):
            data['recordatorio'] = datetime.strptime(data['fecha_recordatorio']+" "+(data['hora_recordatorio'] if 'hora_recordatorio' in data else "00:00:00"),"%Y-%m-%d %H:%M:%S")
        serializer = EventoSerializer(evento ,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk, format=None):
        evento = self.get_object(pk)
        evento.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)