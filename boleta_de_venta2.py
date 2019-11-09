#input
cliente=input("nombre del cliente")
precio_de_las_tijeras=int(input("ingrese el precio de las tijeras:"))
precio_del_pegamento=int(input("ingrese el precio del pegamento:"))
precio_de_cinta=int(input("ingrese el precio de la cinta:"))
#processing
total=(precio_de_las_tijeras+precio_del_pegamento+precio_de_cinta)
#output
print("##################################")
print("#       FARMACIA-ANGEL            ")
print("##################################")
print("#")
print("cliente:",cliente)
print("precio de las tijeras es s/.:",precio_de_las_tijeras)
print("precio del pegamento   es s/.:",precio_del_pegamento)
print("precio de la cinta   es s/. :",precio_de_cinta)
print("precio total es:  s/. ",total)
print("#####################################")
