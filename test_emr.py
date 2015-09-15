from emr import *

N142=Colectivo("Rosario Bus",142,3)
N116=Colectivo("Semtur",116,1)

Tarjeta=Card()
Half=Medio()

def test_cargarNormal():
  Tarjeta.cargar(196)
  assert Tarjeta.getSaldo() == 230

def test_cargarNegativo():
  assert Tarjeta.cargar(-1) == "No se puede cargar un monto negativo"
  
def test_cargarMedio():
  Half.cargar(368)
  assert Half.getSaldo() == 460

def test_boletoNormal():
  #con transbordo
  Tarjeta.boleto(N142,"08/09/2015 00:45")
  Tarjeta.boleto(N116,"08/09/2015 00:55")
  assert Tarjeta.getSaldo() == 222.35

def test_medio():
  #con transbordo
  Half.boleto(N142,"08/09/2015 12:00")
  Half.boleto(N116,"08/09/2015 12:10")
  assert Half.getSaldo() == 456.14

def test_medioOff():
  #medio boleto fuera de horario con transbordo
  Half.boleto(N142,"08/09/2015 02:30")
  Half.boleto(N116,"08/09/2015 02:50")
  assert Half.getSaldo() == 448.49

def test_normalSinsaldo():
  Tarjeta2 = Card()
  Tarjeta2.cargar(5)
  assert Tarjeta2.auxboleto(N142,"08/09/2015 15:30") == False
  assert Tarjeta2.getSaldo() == 5

def test_medioSinsaldo():
  Half2 = Medio()
  Half2.cargar(2)
  assert Half2.auxboleto(N142,"08/09/2015 15:30") == False
  assert Half2.getSaldo() == 2
