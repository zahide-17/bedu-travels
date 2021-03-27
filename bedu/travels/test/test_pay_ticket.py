import unittest
from django.test import TestCase
from rest_framework.test import APIClient
from travels.models import User, Tour, Salida, Boleto
from faker import Faker

class TestComprarBoleto(TestCase):

    #it returns a ticket whiyt status pading when i select oxxo as payment method
    def test_returns_a_ticket_with_status_pending_when_user_select_oxxo_as_payment_method(self):
        user = User(nombre="Pepe", apellidos="Perez", email="nn@gmail.com")
        user.save()
        tour = Tour(nombre="tour 1", descripcion="descripcion")
        tour.save()
        faker = Faker("es_MX")
        fecha_inicio = faker.date_this_month(before_today=False,after_today=True)
        salida = Salida(fechaInicio=fecha_inicio, fechaFin=fecha_inicio, asientos=5, precio=10, tour=tour)
        salida.save()
        client = APIClient()
        response = client.post('/api/buy-ticket/',{'salida_id':salida.id, 'metodo_pago': "oxxo", "usuario_id":user.id})
        ticket =Boleto.objects.get(pk=response.data['id'])
        self.assertContains(response,'status', status_code=201)
        self.assertEqual(response.data['status'],"pending")
        self.assertEqual(ticket.status,'pending')
        self.assertEqual(ticket.metodo_pago, 'oxxo')
        self.assertEqual(ticket.usuario_id, user.id)
        self.assertEqual(ticket.salida_id, salida.id)

       