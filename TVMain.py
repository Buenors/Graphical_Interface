from TV import *

tv = Televisor("SONY", "SONY-123")

controle = ControleRemoto(tv)

controle.sintonizaCanal("MTV")
controle.trocaCanal("MTV")

print(tv.canal_atual)