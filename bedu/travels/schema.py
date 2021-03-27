import graphene
from graphene_django.types import DjangoObjectType
from .models import User,Zona,Tour,Salida

class UserType(DjangoObjectType):
    class Meta:
        model = User

class ZonaType(DjangoObjectType):
    class Meta:
        model = Zona

class TourType(DjangoObjectType):
    class Meta:
        model = Tour
        
class SalidaType(DjangoObjectType):
    class Meta:
        model = Salida


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_zonas = graphene.List(ZonaType)
    all_tours = graphene.List(TourType)
    all_salidas = graphene.List(SalidaType)

    def resolve_all_users(self, info, **Kwargs):
        return User.objects.all()

    def resolve_all_zonas(self, info, **Kwargs):
        return Zona.objects.all()
    
    def resolve_all_tours(self, info, **Kwargs):
        return Tour.objects.all()
    
    def resolve_all_salidas(self, info, **Kwargs):
        return Salida.objects.all()


class CrearZona(graphene.Mutation):
    """ Permite realizar la operación de crear en la tabla Zona """

    class Arguments:
        """ Define los argumentos para crear una Zona """
        nombre = graphene.String(required=True)
        descripcion = graphene.String()
        latitud = graphene.Decimal()
        longitud = graphene.Decimal()

    # El atributo usado para la respuesta de la mutación
    zona = graphene.Field(ZonaType)

    def mutate(self, info, nombre, descripcion=None, latitud=None, longitud=None):
        """
        Se encarga de crear la nueva Zona donde sólo nombre es obligatorio, el
        resto de los atributos son opcionales.
        """
        zona = Zona(
            nombre=nombre,
            descripcion=descripcion,
            latitud=latitud,
            longitud=longitud
        )
        zona.save()

        # Se regresa una instancia de esta mutación y como parámetro la Zona
        # creada.
        return CrearZona(zona=zona)

class EliminarZona(graphene.Mutation):
    """ Permite realizar la operación de eliminar en la tabla Zona """
    class Arguments:
        """ Define los argumentos para eliminar una Zona """
        id = graphene.ID(required=True)

    # El atributo usado para la respuesta de la mutación, en este caso sólo se
    # indicará con la variuable ok true en caso de éxito o false en caso
    # contrario
    ok = graphene.Boolean()

    def mutate(self, info, id):
        """
        Se encarga de eliminar la nueva Zona donde sólo es necesario el atributo
        id y además obligatorio.
        """
        try:
            # Si la zona existe se elimina sin más
            zona = Zona.objects.get(pk=id)
            zona.delete()
            ok = True
        except Zona.DoesNotExist:
            # Si la zona no existe, se procesa la excepción
            ok = False
        # Se regresa una instancia de esta mutación
        return EliminarZona(ok=ok)

class ModificarZona(graphene.Mutation):
    """ Permite realizar la operación de modificar en la tabla Zona """
    class Arguments:
        """ Define los argumentos para modificar una Zona """
        id = graphene.ID(required=True)
        nombre = graphene.String()
        descripcion = graphene.String()
        longitud = graphene.Float()
        latitud = graphene.Float()

    # El campo regresado como respuesta de la mutación, en este caso se regresa
    # la zona modificada.
    zona = graphene.Field(ZonaType)

    def mutate(self, info, id, nombre=None, descripcion=None, longitud=None,
        latitud=None):
        """
        Se encarga de modificar la Zona identificada por el id.
        """
        try:
            # Si la zona existe se modifica
            zona = Zona.objects.get(pk=id)
            # Si algunos de los atributos es proporcionado, entonces se
            # actualiza
            if nombre is not None:
              zona.nombre = nombre
            if descripcion is not None:
              zona.descripcion = descripcion
            if latitud is not None:
              zona.latitud = latitud
            if longitud is not None:
              zona.longitud = longitud
            zona.save()
        except Zona.DoesNotExist:
            # Si la zona no existe, se procesa la excepción
            zona = None
        # Se regresa una instancia de esta mutación
        return ModificarZona(zona=zona)

class Mutaciones(graphene.ObjectType):
    crear_zona =  CrearZona.Field()
    eliminar_zona = EliminarZona.Field()
    modificar_zona = ModificarZona.Field()


schema = graphene.Schema(query=Query, mutation=Mutaciones)


