from django.test import TestCase

from .models import Bares,Tapas

class TestBar(TestCase):

	def test_crear_bar(self):
		bar = Bares(nombre="bar", direccion="direccion",visitas=1)
		bar.save()
		self.assertEqual(bar.nombre, "bar")
		print("Bar creado correctamente")