from emr import *
N142=Colectivo("Rosario Bus",142,3)
N116=Colectivo("Semtur",116,1)
Tarjeta=Card()
Medio=Medio()
def test1():
  Tarjeta.cargar(196)
  assert Tarjeta.saldo() == 230
  Medio.cargar(368)
  assert Medio.cargar() == 460
def test2():
  Tarjeta.boleto(N142,"08/09/2015 00:45")
  Tarjeta.boleto(N116,"08/09/2015 00:55")
  assert Tarjeta.saldo() == 222.35
  Medio.boleto(N142,"08/09/2015 12:00")
  Medio.boleto(N116,"08/09/2015 12:10")
  assert Medio.saldo() == 456.14
  Medio.boleto(N142,"08/09/2015 02:30")
  Medio.boleto(N116,"08/09/2015 02:50")
  assert Medio.saldo() == 448.39
