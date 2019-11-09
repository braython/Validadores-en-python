#INPUT
cliente=input("ingrese el nombre del cliente :")
kg=int(input("ingrese el Nr kg de uvas:"))
pu=float(input("ingrese precio unitario:"))
#PROCESSING
total=(pu*kg)
#VERIFICADOR
comprador_compulsivo=(total>150)
#OUTPUT
print("###############################")
print("#      MERCADO-MARI            ")
print("###############################")
print("#")
print("# cliente: ",cliente)
print("#Item     :",kg,"kg de uvas    ")
print("P.U       : S/.",pu)
print("###############################")
print("comprador compulsivo?:",comprador_compulsivo)
