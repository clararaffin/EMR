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

from datetime import timedelta, datetime

class Colectivo:
  #datos del bondi
	def __init__(self,empresa,linea,interno):
		self.empresa=empresa
		self.linea=linea
		self.interno=interno

class Card:
	def __init__(self):
		self.saldo=0
		self.busprev=0
		self.horabusprev=0
		self.ultimosviajes = Viajes()
		self.historial=[]
		
	def boleto(self,colectivo,hora):
		#normal 5.75
		#transbordo 1.90
		self.flagbondiprev=False
		self.hora=datetime.strptime (hora, "%d/%m/%Y %H:%M")
		if self.busprev!=colectivo.linea and self.flagbondiprev==True and self.hora-self.horabusprev < timedelta(hour=1):
			if self.saldo >= 1.9:
			  	self.saldo=self.saldo-1.9
			  	self.busprev=0
			  	self.horabusprev=0
			  	self.flagbondiprev=False
			  	self.ultimosviajes.viajecito(colectivo,self.hora,1.9)
			  	self.hitorial.append(self.ultimosviajes)
			  	self.ultimosviajes= Viajes()
			  	return True
		else:	  	
			if self.saldo >=5.75:
			  	self.saldo=self.saldo-5.75
				if self.flagbondiprev==False:
					self.flagbondiprev=True
			  	self.busprev=colectivo.linea
			  	self.horabusprev=self.hora
			  	self.ultimosviajes.viajecito(colectivo,self.hora,5.75)
			  	self.hitorial.append(self.ultimosviajes)
			  	self.ultimosviajes= Viajes()
			  	return True
			else:
			  	return False
		
	#recargar
	def cargar(self,monto):
		self.monto=monto
		if self.monto==196:
			self.saldo=self.saldo+230
		elif self.monto==368:
			self.saldo=self.saldo+460
		else:
			self.saldo=self.saldo+self.monto
	#historial
	def ViajesRealizados(self):
		for historial in self.historial:
			print(str(historial.linea)+"/t"+str(historial.empresa)+"/t"+str(historial.interno)+"/t"+str(historial.hora)+"/t"+str(historial.monto))
	#saldo
	def saldo(self):
		return self.saldo

class Medio(Card):
  #normal 2.90
  #transbordo 0.96
  def medioBoleto(self,colectivo,hora):
  	self.flagbondiprev=False
  	self.hora=datetime.strptime (hora, "%d/%m/%Y %H:%M")
  	if self.hora.time().hour >= 6 and self.hora.time().hour <= 0:
	  	if self.busprev!=colectivo.linea and self.flagbondiprev==True and self.hora-self.horabusprev < timedelta(hour=1):
		  if self.saldo >= 0.96:
			self.saldo=self.saldo-0.96
			self.busprev=0
			self.horabusprev=0
			self.flagbondiprev=False
			self.ultimosviajes.viajecito(colectivo,self.hora,0.96)
			self.hitorial.append(self.ultimosviajes)
			self.ultimosviajes= Viajes()
			return True
		else:
		  if self.saldo >=2.9:
			self.saldo=self.saldo-2.9
			self.busprev=colectivo.linea
			self.horabusprev=self.hora
			self.ultimosviajes.viajecito(colectivo,self.hora,2.9)
			self.hitorial.append(self.ultimosviajes)
			self.ultimosviajes= Viajes()
			return True
  	else:
  		self.boleto(colectivo,hora)
class Viajes:
  #datos del viaje
	def __init__ (self):
		self.hora=0
		self.monto=0
		self.empresa=""
		self.linea=0
		self.interno=0
		
	def viajecito(self,colectivo,hora,monto):
		self.hora=hora
		self.monto=monto
		self.empresa=colectivo.empresa
		self.linea=colectivo.linea
		self.interno=colectivo.interno
