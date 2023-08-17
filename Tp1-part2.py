"""
    #Ejercicio1
base = float(input("Ingrese el valor de la baase del rectangulo: "))
altura = float(input("Ingrese el valor de la altura del rectángulo: "))

area_rectangulo = base*altura
perim_rectangulo = (base*2)+(altura*2)

print(f'El area del rectangulo es: {area_rectangulo}. \nEl perimetro del rectangulo es: {perim_rectangulo}')

#Ejercicios 4, 11, 18

#4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
# C = (F-32)*5/9

farenh = float(input("Ingrese los grados fahrenheit: "))
celsius = (farenh-32)*5/9
print(f"El equivalente en celsius de {farenh}°F es: {celsius}°C")

#11. Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo). 

num1 = float(input("Ingrese numero 1: "))
num2 = float(input("Ingrese numero 2: "))

dist = abs(num1 - num2)

print(f"La distancia entre {num1} y {num2} es: {dist}")
"""

#18

valor_cena = float(input("Ingrese el valor de la cena: "))
cost_serv = (valor_cena * 6.2)/100
propi = (valor_cena * 10)/100
print(f"El valor de la cena, sumando el costo de servicio y la propina es: {valor_cena + cost_serv + propi}")


