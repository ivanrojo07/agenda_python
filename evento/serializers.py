from rest_framework import serializers
from .models import Evento
class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields=(
            'id',
            'empresa_id',
            'sucursal_id',
            'usuario_id',
            'supervisor_id',
            'project_id',
            'contacto_id',
            'titulo',
            'descripcion',
            'direccion',
            'latitud',
            'longitud',
            'tipo_evento',
            'fecha_registro',
            'inicio',
            'get_fecha_inicio',
            'get_hora_inicio',
            'fin',
            'get_fecha_fin',
            'get_hora_fin',
            'recordatorio',
            'temporizador',
            'recurrente',
            'periodo',
            'url',
            'created_at',
            'updated_at',
        )