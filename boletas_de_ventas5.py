#input
cliente=input("nombre del cliente")
precio_del_libro=int(input("ingrese el precio del libro:"))
precio_del_borrador=int(input("ingrese el precio del borrador:"))
precio_del_tajador=int(input("ingrese el precio del tajador :"))
#processing
total=(precio_del_libro+precio_del_borrador+precio_del_tajador)
#output
print("##################################")
print("#       LIBRERIA-JUANA            ")
print("##################################")
print("#")
print("cliente:",cliente)
print("precio de la mermelada es s/.:",precio_del_libro)
print("precio de la mantequilla es s/.:",precio_del_borrador)
print("precio de las galletas   es s/. :",precio_del_tajador)
print("precio totales:  s/. ",total)
print("#####################################")
