#input
cliente=input("nombre del cliente")
precio_de_pastillas=int(input("ingrese el precio de pastillas:"))
precio_del_jarabe=int(input("ingrese el precio del jarabe:"))
precio_del_suero=int(input("ingrese el precio del suero :"))
#processing
total=(precio_de_pastillas+precio_del_jarabe+precio_del_suero)
#output
print("##################################")
print("#       FARMACIA-ANGEL            ")
print("##################################")
print("#")
print("cliente:",cliente)
print("precio de pastillas es s/.:",precio_de_pastillas)
print("precio del jarabe   es s/.:",precio_del_jarabe)
print("precio del suero    es s/. :",precio_del_suero)
print("precio totales:  s/. ",total)
print("#####################################")
