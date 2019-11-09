
#calculadora nro4
#esta calculadora realiza el calculo de la fuerza final

#declaracion de variables
velocidad_inicial,velocidad_final,aceleracion,tiempo=0.0,0.0,0.0,0.0

#calculadora
velocidad_inicial=56
aceleracion=9.8
tiempo=4
velocidad_final=(velocidad_final+(aceleracion*tiempo))
#mostrar datos
print("velocidad_inical= ",velocidad_inicial)
print("aceleracion= ",aceleracion)
print("velocida_final= ",velocidad_final)
#verificador
velocidad_reducida=( velocidad_final < 26)
print("la velocidad final del auto  es  reducidad ? :",velocidad_reducida)
