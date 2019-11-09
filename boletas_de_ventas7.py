#input
cliente=input("nombre del cliente")
precio_del_polo=int(input("ingrese el precio del polo:"))
precio_del_pantalon=int(input("ingrese el precio del pantalon:"))
precio_del_chaleco=int(input("ingrese el precio del chaleco:"))
#processing
total=(precio_del_polo+precio_del_pantalon+precio_del_chaleco)
#output
print("##################################")
print("#      TIENDA-RIPLEY           ")
print("##################################")
print("#")
print("cliente:",cliente)
print("precio del polo es s/.:",precio_del_polo)
print("precio del pantalon es s/.:",precio_del_pantalon)
print("precio del chaleco  es s/. :",precio_del_chaleco)
print("precio totales:  s/. ",total)
print("#####################################")
