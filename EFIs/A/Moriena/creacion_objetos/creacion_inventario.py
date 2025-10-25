from inventario.inventario_j import Inventario
from items.clase_equipamiento import Equipamiento,Casco,Pechera,Arma
from items.pociones import PocionVida,PocionStamina,PocionFuerza

#Pociones Vida
pocion_vida_t1 = PocionVida(1)
pocion_vida_t2 = PocionVida(2)
pocion_vida_t3 = PocionVida(3)
#Pociones Stamina
pocion_stamina_t1 = PocionStamina(1)
pocion_stamina_t2 = PocionStamina(2)
pocion_stamina_t3 = PocionStamina(3)
#Armas
garrote_infernal = Arma("Garrote Infernal","A",30)
espadita = Arma("Espadita","B",10000000000000)
#cascos
casco_hades = Casco("Casco de Hades","B",20)
casco_hola = Casco("Casco de hola","B",20)


#inventario inicial_barbaro
#arma
garrote = Arma("Garrote","C",10)

lista_objetos_barbaro =[garrote,
                        pocion_vida_t1,
                        pocion_vida_t1,
                        pocion_vida_t1,
                        pocion_stamina_t1,
                        pocion_vida_t2,
                        pocion_stamina_t1,
                        pocion_stamina_t3,
                        pocion_stamina_t1
                        ]

inventario_inicial_barbaro = Inventario(lista_objetos_barbaro)

#inventario inicial_mago
#
baston = Arma("Baston","C",10)
lista_objetos_mago = [garrote,
                      baston,pocion_vida_t1,
                      pocion_vida_t1,
                      pocion_vida_t1,
                      pocion_stamina_t1,
                      pocion_vida_t2,
                      pocion_stamina_t1,
                      pocion_stamina_t3,
                      pocion_stamina_t1
                      ]

inventario_inicial_mago = Inventario(lista_objetos_mago)