#input
cliente=input("nombre del cliente")
precio_de_mermelada=int(input("ingrese el precio de la mermelada:"))
precio_de_mantequilla=int(input("ingrese el precio de la mantequilla"))
precio_de_galletas=int(input("ingrese el precio de las galletas"))
#processing
total=(precio_de_mantequilla+precio_de_mermelada+precio_de_galletas)
#output
print("##################################")
print("#       BODEGA-DON MIGUEL         ")
print("##################################")
print("#")
print("cliente:",cliente)
print("precio de la mermelada es s/.:",precio_de_mermelada)
print("precio de la mantequilla es s/.:",precio_de_mantequilla)
print("precio de las galletas   es s/. :",precio_de_galletas)
print("precio totales:  s/. ",total)
print("#####################################")
