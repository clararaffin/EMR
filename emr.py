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
		self.flagbondiprev=False
		self.ultimosviajes = Viajes()
		self.historial=[]
		
		
	def boleto(self,colectivo,hora):
		self.auxboleto(colectivo,hora)
		
	def auxboleto(self,colectivo,hora):
		
		#normal 5.75
		#transbordo 1.90
		self.hora=datetime.strptime (hora, "%d/%m/%Y %H:%M")
		if self.busprev!=colectivo.linea and self.flagbondiprev==True and self.hora-self.horabusprev < timedelta(minutes=60):
			if self.saldo >= 1.9:
			  	self.saldo=self.saldo-1.9
			  	self.busprev=0
			  	self.horabusprev=0
			  	self.flagbondiprev=False
			  	self.ultimosviajes.viajecito(colectivo,self.hora,1.9)
			  	self.historial.append(self.ultimosviajes)
			  	self.ultimosviajes= Viajes()
			  	return True
		else:	  	
			if self.saldo >=5.75:
				self.saldo=self.saldo-5.75
				if self.flagbondiprev == False:
					self.flagbondiprev = True
				self.busprev=colectivo.linea
				self.horabusprev=self.hora
				self.ultimosviajes.viajecito(colectivo,self.hora,5.75)
				self.historial.append(self.ultimosviajes)
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
	def getSaldo(self):
		return self.saldo

class Medio(Card):
  
	def boleto(self,colectivo,hora):
		self.hora=datetime.strptime (hora, "%d/%m/%Y %H:%M")
		if self.hora.time().hour <= 6 and self.hora.time().hour >= 0:
			self.auxboleto(colectivo,hora)
		else:
			if self.busprev!=colectivo.linea and self.flagbondiprev==True and self.hora-self.horabusprev < timedelta(minutes=60):
				if self.saldo >= 0.96:
					self.saldo=self.saldo-0.96
					self.busprev=0
					self.horabusprev=0
					self.flagbondiprev=False
					self.ultimosviajes.viajecito(colectivo,self.hora,0.96)
					self.historial.append(self.ultimosviajes)
					self.ultimosviajes= Viajes()
					return True
			else:
				if self.saldo >=2.9:
					self.saldo=self.saldo-2.9
					if self.flagbondiprev == False:
						self.flagbondiprev = True
					self.busprev=colectivo.linea
					self.horabusprev=self.hora
					self.ultimosviajes.viajecito(colectivo,self.hora,2.9)
					self.historial.append(self.ultimosviajes)
					self.ultimosviajes= Viajes()
					return True
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
