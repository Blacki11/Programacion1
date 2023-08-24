#Solicitar al usuario que ingrese fecha en formato "dia, DD/MM"

dia=input ("Ingrese el dia: ").lower()
num1=int(input ("Ingrese la fecha: "))
num2=int(input ("Ingrese el mes: "))
dias_semana=["lunes", "martes", "miercoles", "jueves", "viernes"]
if(dia) not in dias_semana:
    print("dia erroneo")
elif(num1)<1 or num1>31:
    print("Fecha erronea")
elif(num2)<1 or num2>12:
    print("mes erroneo")
else:
    print(dia, ",", num1, "/", num2)
    if dia in ["lunes", "martes", "miercoles"]:     #Se solicita informacion para saber si en estos dias se tomaron examenes.
            examenes1=(input("Se tomaron examenes?(Si/No): ")).lower()
            if (examenes1=="si"):
                aprob=int(input("Ingrese la cantidad de alumnos aprobados: "))
                desap=int(input("Ingrese la cantidad de alumnos desaprobados: "))
                sumalum = (aprob + desap)
                p_aprob = (aprob/sumalum)*100
                print('El porcentaje de alumnos aprobados fue', (p_aprob), "%")
            elif(examenes1=="no"):
                print("No se tomaron examenes ese dia para ese nivel")
            else:
                print("Respuesta Invalida")
    elif dia in ["jueves"]:              #Se solicita el % de alumnos que asisten a clase
            porc_asist=float(input("Ingrese el porcentaje de alumnos que asistieron a clase: "))
            if porc_asist>50:
                print("Asistio la mayoria")
            else:
                print("No asistio la mayoria")
    elif dia in ["viernes"] and (num2==1 or num2==7) and num1 == 1:               #Comienzo de ciclo de "Ingles para viajeros"
            cant_alumn=int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            aranc_alumn=float(input("Ingrese el arancel por alumno: "))
            ingTot=cant_alumn*aranc_alumn
            print("Ingreso total: $", ingTot)
            print("Comienza un nuevo ciclo")
    else:
            print("Nivel no reconocido")
