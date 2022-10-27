#2. Solicite al usuario la temperatura en grados celcius y conviertala a farenheit, kelvin y rankie

gradosc= float(input("Ingrese la temperatura en grados celcius:   "))
gradosf=gradosc*1.8+32
gradosk=gradosc+273.15
gradosr=gradosc*1.8+491.67

print("La temperatura ",gradosc,"°C"," convertida en Farenheit es: ",gradosf,"°F",sep="")
print("La temperatura ",gradosc,"°C"," convertida en Kelvin es: ",gradosk,"°K",sep="")
print("La temperatura ",gradosc,"°C"," convertida en Rankie es: ",gradosr,"°R",sep="")