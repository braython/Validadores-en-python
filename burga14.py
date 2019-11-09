#calculadora nro14
#esta clculadora realiza calculo de la presion hidrostatica

#declaracion de datos
densidad_liquido,gravedad,altura,presion_hidrostatica=0.0,0.0,0.0,0.0

#calculadora
densidad_liquido=13.9
gravedad=9.8
altura=6
presion_hidrostatica=((densidad_liquido*gravedad)*altura)
#mostrar datos
print("densidad del liquido= ",densidad_liquido)
print("gravedad= ",gravedad)
print("altura= ",altura)
print("presion hidrostatica= ",presion_hidrostatica)
#verificador
presion_hidrostatica_aumentada=(presion_hidrostatica >456 )
print("la presion hidrostatica del liquido  es aumentada? :",presion_hidrostatica_aumentada)
