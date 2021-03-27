from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import UserSerializer, ZonaSerializer, TourSerializer, SalidaSerializer
from .models import Tour, Zona, User, Salida, Boleto
from rest_framework import viewsets,status
from rest_framework. response import Response
from rest_framework.views import APIView

# Create your views here.
@login_required()
def index(request):
    """Vsta para atender la peticion de la url /"""
    #Obteniedno los datos mediantes consultas
    tours = Tour.objects.all()
    zonas = Zona.objects.all()
    es_editor = request.user.groups.filter(name="editores").exists()
    return render(request,"tours/index.html",{'tours': tours, "zonas":zonas, "es_editor":es_editor})

@login_required()
def eliminar_tour(request, idTour):
    """
    Atiende la petición GET
       /tour/eliminar/<int:idTour>/
    """
    # Se obtienen los objetos correspondientes a los id's
    tour = Tour.objects.get(pk=idTour)

    # Se elimina el tour
    tour.delete()

    return redirect("/")

#va a serializar la informacion en json.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all().order_by('id')
    serializer_class = ZonaSerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all().order_by('id')
    serializer_class = TourSerializer

class SalidaViewSet(viewsets.ModelViewSet):
    queryset = Salida.objects.all().order_by('id')
    serializer_class = SalidaSerializer

class BuyTicket(APIView):
    def post(self,request):
        print(vars(request))
        if request.data["metodo_pago"] == "oxxo":
            ticket_status = "pendind"
        else:
            tichet_status = "approved"

        ticket= Boleto(metodo_pago= request.data["metodo_pago"],
                       usuario_id=request.data["usuario_id"], 
                       salida_id= request.data["salida_id"],
                       status=ticket_status)
        ticket.save()
        return Response({'id':ticket.id, 'status':ticket.status}, status=status.HTTP_201_CREATED)





# def login_user(request):
#     """ Atiende las peticiones de GET /login/ """
#     # Si hay datos vía POST se procesan
#     if request.method == "POST":
#         # Se obtienen los datos del formulario
#         username = request.POST["username"]
#         password = request.POST["password"]
#         next = request.GET.get("next", "/")
#         acceso = authenticate(username=username, password=password)
#         if acceso is not None:
#             # Se agregan datos al request para mantener activa la sesión
#             login(request, acceso)
#             # Y redireccionamos a next
#             return redirect(next)
#         else:
#             # Usuario malo
#             msg = "Datos incorrectos, intente de nuevo!"
#     else:
#         # Si no hay datos POST
#         msg = "Request invalido"
#     return render(request, "registration/login.html")

# def logout_user(request):
#     """ Atiende las peticiones de GET /logout/ """
#     # Se cierra la sesión del usuario actual
#     logout(request)

#     return redirect("/login/")


