from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from .models import User,Zona,Tour, Salida

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = ('id','nombre','apellidos','email','fechaNacimiento','genero','tipo','clave')

class Zona2Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= Zona
        fields = ('id','nombre')

class TourSerializer(serializers.HyperlinkedModelSerializer):
    zonaSalida = Zona2Serializer(read_only=True)
    zonaLlegada = Zona2Serializer(read_only=True)

    class Meta:
        model= Tour
        fields = ('id','nombre','slug','operador','tipoDeTour','descripcion','img','pais','zonaSalida','zonaLlegada','salidas')

class SalidaSerializer(serializers.HyperlinkedModelSerializer):
    salida_tour = TourSerializer(many=True, read_only=True)

    class Meta:
        model = Salida
        fields =  ('id', 'fechaInicio', 'fechaFin', 'asientos', 'precio', 'tour','salida_tour')

class ZonaSerializer(serializers.HyperlinkedModelSerializer):
    tours_salida = TourSerializer(many=True, read_only=True)
    tours_llegada = TourSerializer(many=True, read_only=True)

    class Meta:
        model= Zona
        fields = ('id','nombre','descripcion','longitud','latitud','tours_salida','tours_llegada')
