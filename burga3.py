#calculadora nro3
#esta calculadora realiza el calculo de un trapecio

#delaracion de variables
base_mayor,base_menor,altura=0.0,0.0,0.0

#calculadora
base_mayor=38
base_menor=18
altura=8
area_del_trapecio= ((base_mayor+base_menor)*altura)/2
#mostrar datos
print("base mayor= ", base_mayor)
print("base menor= ", base_menor)
print("area_del_trapecio= ", area_del_trapecio)

#verificador
altura_elevada=(altura>50)
print("la altura de del trapecio es elevada? :",altura_elevada)
