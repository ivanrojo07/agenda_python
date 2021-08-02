from django.db import models

# Create your models here.
class Evento(models.Model):
    empresa_id = models.BigIntegerField(null=True,blank=True)
    sucursal_id = models.BigIntegerField(null=True,blank=True)
    usuario_id = models.BigIntegerField()
    supervisor_id = models.BigIntegerField(null=True,blank=True)
    project_id = models.BigIntegerField(null=True, blank=True)
    contacto_id = models.BigIntegerField(null=True, blank=True)

    titulo = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=255,blank=True, null=True)
    latitud = models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=7)
    longitud = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=7)
    tipo_evento = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    inicio = models.DateTimeField(blank=True,null=True)
    fin = models.DateTimeField(blank=True, null=True)
    recordatorio = models.DateTimeField(blank=True, null=True)
    temporizador = models.TimeField(blank=True,null=True)
    recurrente = models.CharField(max_length=255, blank=True, null=True)
    periodo = models.CharField(max_length=255,blank=True,null=True)
    url = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_created=True, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ("-created_at",)
    
    def __str__(self):
        return self.titulo
    
    def get_fecha_inicio(self):
        if(self.inicio is not None):
            return self.parse_datetime(self.inicio,'%Y-%m-%d')
    def get_fecha_fin(self):
        if(self.fin is not None):
            return self.parse_datetime(self.inicio,'%Y-%m-%d')

    def get_hora_inicio(self):
        if(self.inicio is not None):
            return self.parse_datetime(self.inicio,'%H:%M')
    def get_hora_fin(self):
        if(self.fin is not None):
            return self.parse_datetime(self.fin,'%H:%M')
    def parse_datetime(self,datetime,format):
        return datetime.strftime(format)
