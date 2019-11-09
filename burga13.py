#calculadora nro13
#esta calculadora realiza calculo de energia potencial gravitatoria

#declaracion de datos
masa,gravedad,altura,energia_potencial_gravitatoria=0.0,0.0,0.0,0.0

#calculadora
masa=93
gravedad=9.8
altura=32
energia_potencial_gravitatoria=((masa*gravedad)*altura)
#mostrar datos
print("masa= ", masa)
print("gravedad= ",gravedad)
print("altura= ",altura)
print("energia potencial= ",energia_potencial_gravitatoria)
#verificador
energia_potencial_disminuida=( energia_potencial_gravitatoria<852 )
print("la energia potenial gravitatotia es disminuida? :",energia_potencial_disminuida)

