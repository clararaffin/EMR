from emr import *

N142=Colectivo("Rosario Bus",142,3)
N116=Colectivo("Semtur",116,1)
Tarjeta=Card()
Medio=Medio()
def test_cargar():
  Tarjeta.cargar(196)
  assert (Tarjeta.getSaldo() == 230)
  Medio.cargar(368)
  assert (Medio.getSaldo() == 460)
def test_boleto():
  Tarjeta.boleto(N142,"08/09/2015 00:45")
  Tarjeta.boleto(N116,"08/09/2015 00:55")
  assert Tarjeta.getSaldo() == 222.35
  Medio.boleto(N142,"08/09/2015 12:00")
  Medio.boleto(N116,"08/09/2015 12:10")
  assert Medio.getSaldo() == 456.14
  Medio.boleto(N142,"08/09/2015 02:30")
  Medio.boleto(N116,"08/09/2015 02:50")
  assert Medio.getSaldo() == 448.39
