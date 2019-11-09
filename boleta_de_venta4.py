#input
cliente=input("nombre del cliente:")
precio_del_pan=int(input("ingrese el precio del pan es :"))
precio_de_pie=int(input("ingrese el precio del pie es :"))
precio_de_yogurt=int(input("ingrese el precio del yogurt:"))
#processing
total=(precio_del_pan+precio_de_pie+precio_de_yogurt)
#output
print("##################################")
print("#       PANADERIA-SAN CARLOS          ")
print("##################################")
print("#")
print("cliente:",cliente)
print("precio del pan es s/.:",precio_del_pan)
print("precio del pie es s/.:",precio_de_pie)
print("precio del yogurt  es s/. :",precio_de_yogurt)
print("precio totales:  s/. ",total)
print("#####################################")
