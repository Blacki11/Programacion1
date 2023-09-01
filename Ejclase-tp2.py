#Ejercicio 1

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

corr = int(input("Ingrese la cantidad de lugares para el corrimiento: "))

for i in range(5):
    mensaje = input(f"Ingrese el mensaje {i + 1}: ")
    mensaje_encr = ""

    
    for letra in mensaje:
        if letra.isalpha():
            letra = letra.upper()
            indice = alfabeto.index(letra)
            nuevo_indice = (indice + corr) % 26
            nueva_letra = alfabeto[nuevo_indice]
            mensaje_encr += nueva_letra
        else:
            mensaje_encr += letra


    print(f"Mensaje encriptado {i + 1}: {mensaje_encr}")

#Ejercicio 2

dig_par=0
dig_impar=0

while True:
    num1=int(input('Ingrese numeros enteros positivos(0 para salir): '))

    if num1==0:
        break
    dig_num = str(num1)
    
    for digito in dig_num:
        if int(digito) % 2 == 0:
            print(f'El dígito {digito} en el número {dig_num} es par')
            dig_par += 1
        else:
            print(f'El dígito {digito} en el número {dig_num} es impar')
            dig_impar += 1

print(f'Total de dígitos pares: {dig_par}')
print(f'Total de dígitos impares: {dig_impar}') 