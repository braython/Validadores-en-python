#input
cliente=input("nombre del cliente")
precio_de_clavos=int(input("ingrese el precio de clavos:"))
precio_del_fierro=int(input("ingrese el precio del fierro:"))
precio_del_martillo=int(input("ingrese el precio del martillo :"))
#processing
total=(precio_de_clavos+precio_del_fierro+precio_del_martillo)
#output
print("##################################")
print("#       FERRETERIA-OLMOS            ")
print("##################################")
print("#")
print("cliente:",cliente)
print("precio de clavos es s/.:",precio_de_clavos)
print("precio del fierro es s/.:",precio_del_fierro)
print("precio del martillo es s/. :",precio_del_martillo)
print("precio totales:  s/. ",total)
print("#####################################")
