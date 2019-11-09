#input
cliente=input("nombre del cliente")
precio_de_computadora=int(input("ingrese el precio de la computadora:"))
precio_de_laptop=int(input("ingrese el precio de la laptop :"))
precio_del_celular=int(input("ingrese el precio del celular :"))
#processing
total=(precio_de_computadora+precio_de_laptop+precio_del_celular)
#output
print("############################################")
print("#  TIENDA DE ELECTRODOMESTICOS - ELECTRA ")
print("##################################")
print("#")
print("cliente:",cliente)
print("precio de la computadora es s/.:",precio_de_computadora)
print("precio de la laptop   es s/.:",precio_de_laptop)
print("precio del celular  es s/. :",precio_del_celular)
print("precio totales:  s/. ",total)
print("#############################################")
