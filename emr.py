"""
El EMR (Ente de Movilidad de Rosario) está interesado en modernizar su software de gestión de tarjetas
magnéticas. En esta primera etapa están buscando construir un software que permita simular el funcionamiento de
una tarjeta magnética en los siguientes escenarios:

1) Tarjeta.PagarBoleto(colectivo, horario)
2) Tarjeta.Recarga(monto)
3) Tarjeta.Saldo()
4) Tarjeta.ViajesRealizados()

Considerar las siguientes restricciones
Existen dos tipos de tarjeta:
TarjetaComun: Paga el boleto a 5.75 y el transbordo a 1.90
TarjetaMedioBoleto: Paga el boleto a 2.90 y el transbordo a 0,96
"""
from datetime import datetime, timedelta, time
now = datetime.now()

class Card:
	def __init__(self):
		self.saldo = 0
		self.busprev = 0
		self.horabusprev = 0
		self.flagbondiprev = False
		
		def Boleto():
		  #normal 5.75
		  #transbordo 1.90
		
		#recargar
		#historial
		#saldo

class Medio(Card):
  #normal 2.90
  #transbordo 0.96
  
class Viajes:
  #datos del viaje
class Bondi:
  #datos del bondi
