"""Programa.py
Programa que convierte numeros de base a decimal y viceversa
Desarrollado por: Luis Alejandro Canchola Pedraza


"""
from os import system
import time
import math
import sys
def limpia(lista):
    cadena = "".join([str(_) for _ in lista])
    cadena=cadena[::-1]
    return (cadena)  
#parte que convierte de base X a decimal
def binario2Dec (cadena):
    exp=[1,2,4,8,16,32,64,128,256,512,1024,2049,4096,8192]
    numero=[]
    cadena=cadena[::-1]
    for i in range(len(cadena)):
        numero.append(cadena[i])
    resultado=0
    for j in range(len(numero)):
        operador=int(numero[j])*exp[j]
        resultado=resultado+operador
    return resultado

    
def quinario2Dec(cadena):
    base=5
    exp=[pow(base,0),pow(base,1),pow(base,2),pow(base,3),pow(base,4),pow(base,5),pow(base,6),pow(base,7),pow(base,8),pow(base,9),pow(base,10),pow(base,11)]
    numero=[]
    #['4', '1', '0', '2']
    cadena=cadena[::-1]
    for i in range(len(cadena)):
        numero.append(cadena[i])
    resultado=0
    for j in range(len(numero)):
        operador=int(numero[j])*exp[j]
        resultado=resultado+operador
    return resultado
def hexadecimal2Dec(cadena):
    base=16
    exp=[pow(base,0),pow(base,1),pow(base,2),pow(base,3),pow(base,4),pow(base,5),pow(base,6),pow(base,7),pow(base,8),pow(base,9),pow(base,10),pow(base,11)]
    numero=[]
    cadena=cadena[::-1]
    for i in range(len(cadena)):
        numero.append(cadena[i])
    resultado=0
    bandera=True
    conv=[]
    for e in range(len(numero)):
        if(numero[e]=="A"):
            conv.append(10)
        elif(numero[e]=="B"):
            conv.append(11)
        elif(numero[e]=="C"):
            conv.append(12)
        elif(numero[e]=="D"):
            conv.append(13)
        elif(numero[e]=="E"):
            conv.append(14)
        elif(numero[e]=="F"):
            conv.append(15)
        else:
            conv.append(numero[e])
    for j in range(len(conv)):
        operador=int(conv[j])*exp[j]
        resultado=resultado+operador
    return resultado
def octal2Dec (cadena):
    base=8
    exp=[pow(base,0),pow(base,1),pow(base,2),pow(base,3),pow(base,4),pow(base,5),pow(base,6),pow(base,7),pow(base,8),pow(base,9),pow(base,10),pow(base,11)]
    numero=[]
    cadena=cadena[::-1]
    for i in range(len(cadena)):
        numero.append(cadena[i])
    resultado=0
    for j in range(len(numero)):
        operador=int(numero[j])*exp[j]
        resultado=resultado+operador
    return resultado
#parte que convierte de decimal a base
def Dec2binario (numero):
    resto=""
    bandera=True
    binario=[]
    temp=int(numero)
    while(bandera):
        if((temp/2) != 0):
            binario.append(temp%2)
            temp=math.floor(temp/2)
            bandera=True
        elif((numero) == 0):
            binario.append(0)
            bandera=False
        else:
            bandera=False
            """
                    elif(numero==1):
            binario.append(numero%2)
            binario.append(0)
            bandera=False"""

    resto=limpia(binario)
    #resto=resto[::-1]
    return resto
def Dec2quinario(numero):
    resto=""
    bandera=True
    quinario=[]
    temp=int(numero)
    while(bandera):
        if((temp/5) != 0):
            quinario.append(temp%5)
            #numero=numero/5
            temp=math.floor(temp/5)
            bandera=True
        elif((numero) == 0):
            quinario.append(0)
            bandera=False
        else:
            bandera=False
    resto=limpia(quinario)
    #resto=resto[::-1]
    return resto
def Dec2hexadecimal(numero):
    resto=""
    bandera=True
    Hexadecimalfeo=[]
    temp=int(numero)
    while(bandera):
        if((temp/16) != 0):
            Hexadecimalfeo.append(temp%16)
            temp=math.floor(temp/16)
            bandera=True
        elif((numero) == 0):
            Hexadecimalfeo.append(0)
            bandera=False
        else:
            bandera=False
    Hexadecimal=[]
    for e in range(len(Hexadecimalfeo)):
        if(Hexadecimalfeo[e]==10):
            Hexadecimal.append("A")
        elif(Hexadecimalfeo[e]==11):
            Hexadecimal.append("B")
        elif(Hexadecimalfeo[e]==12):
            Hexadecimal.append("C")
        elif(Hexadecimalfeo[e]==13):
            Hexadecimal.append("D")
        elif(Hexadecimalfeo[e]==14):
            Hexadecimal.append("E")
        elif(Hexadecimalfeo[e]==15):
            Hexadecimal.append("F")
        else:
            Hexadecimal.append(Hexadecimalfeo[e])
    resto=limpia(Hexadecimal)
    return resto
def Dec2octal (numero):
    resto=""
    bandera=True
    Octal=[]
    temp=int(numero)
    while(bandera):
        if((temp/8) != 0):
            Octal.append(temp%8)
            #numero=numero/5
            temp=math.floor(temp/8)
            bandera=True
        elif((numero) == 0):
            octal.append(0)
            bandera=False
        else:
            bandera=False
    resto=limpia(Octal)
    return resto
#Comprobar que los numeros introducidos sean de la base
def verificar(numero,base):
    cadena=[]
    for i in range(len(numero)):
        cadena.append(numero[i])
    error=numero.isdigit()
    Binario=[0,1]
    Quinario=[0,1,2,3,4]
    Octal=[0,1,2,3,4,5,6,7]
    Decimal=[0,1,2,3,4,5,6,7,8,9]
    hexadecimal=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    if(base=="Binario" and error==True):
        bina="01"
        bandera=True
        e=0
        while(bandera):
            if(len(numero)==1):
                if ((str(numero) not in bina)):
                    bandera=False
                    return False
                elif (int(cadena[e]) in Binario):
                    bandera= True   
                    return True
            else:
                for e in range(len(cadena)):
                    for k in range(len(Binario)):
                        if (int(cadena[e]) in Binario):
                            bandera= True
                            return True
                        else:

                            print(f"El digito {cadena[e]} no pertenece a la base {base}")
                            bandera=False
                            time.sleep(3)
                            
                            return False
        return True       
    elif(base=="Quinario"and error==True):
        Quin="01234"
        bandera=True
        e=0
        while(bandera):
            if(len(numero)==1):
                if ((str(numero) not in quin)):
                    bandera=False
                    return False
                else:
                    for e in range(len(cadena)):
                        for k in range(len(Quinario)):
                            if (int(cadena[e]) in Quinario):
                                bandera= True   
            else:
                for e in range(len(cadena)):
                    for k in range(len(Quinario)):
                        if (int(cadena[e]) in Quinario):
                            bandera= True
                        else:
                            print(f"El digito {cadena[e]} no pertenece a la base {base}")
                            bandera=False
                            time.sleep(3)
                            return False
        return True                
    elif(base=="Octal"and error==True):
        Oct="01234567"
        bandera=True
        e=0
        while(bandera):
            if(numero in Oct):
                bandera=False
            else:
                for e in range(len(cadena)):
                    for k in range(len(Octal)):
                        if (int(cadena[e]) in Octal):
                            bandera= True
                        else:
                            print(f"El digito {cadena[e]} no pertenece a la base {base}")
                            bandera=False
                            time.sleep(3)
                            return False
        return True     
    elif(base=="Decimal"and error==True):
        Dec="0123456789"
        bandera=True
        e=0
        while(bandera):
            if(numero in Dec):
                bandera=False
            else:
                for e in range(len(cadena)):
                    for k in range(len(Decimal)):
                        if (int(cadena[e]) in Decimal):
                            bandera= True
                        else:
                            print(f"El digito {cadena[e]} no pertenece a la base {base}")
                            bandera=False
                            time.sleep(3)
                            return False
        return True           
    elif(base=="Hexadecimal"):
        Hexa="0123456789ABCDEF"
        bandera=True
        e=0
        while(bandera):
            if(numero in Hexa):
                bandera=False
            else:
                for e in range(len(cadena)):
                    for k in range(len(hexadecimal)):
                        if (int(cadena[e]) in hexadecimal):
                            bandera= True
                        else:
                            print(f"El digito {cadena[e]} no pertenece a la base {base}")
                            bandera=False
                            return False
        return True     
    else:
        print(f"Error \"{numero}\" no pertenece a la base {base}")
        bandera=False 
        time.sleep(3)
        return bandera      



#instrucciones Switch case
def Decimal():
    flag=True
    while(flag):
        system("cls")
        print("--------------------------------------------Convertir desde Decimal a ???---------------------------------------")
        print("")
        print("\t\t\t¿A que base quieres convertir?\t\t\t")
        print("\t\t\t1. Binario")
        print("\t\t\t2. Quinario")
        print("\t\t\t3. Hexadecimal")
        print("\t\t\t4. Octal")
        print("\t\t\t5. Regresar al menu")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------")
        opcion=str(input())
        if(opcion=='1'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Decimal a Binario--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Decimal")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Decimal a Binario--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Binario es {Dec2binario(numero)}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            Decimal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='2'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Decimal a Quinario--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Decimal")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Decimal a Quinario--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Quinario es {Dec2quinario(numero)}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            Decimal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='3'):
            flag=True
            while(flag):
                system("cls")
                print("----------------------------------------Convertir desde Decimal a Hexadecimal----------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Decimal")
                if(bandr!=False):
                    system("cls")
                    print("-------------------------------------Convertir desde Decimal a Hexadecimal-------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Hexadecimal es {Dec2hexadecimal(numero)}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            Decimal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='4'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Decimal a Octal--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Decimal")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Decimal a Octal--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Octal es {Dec2octal(numero)}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            Decimal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='5'):
            print("Regresando al menu anterior")
            main()
        else:
            print("Opcion no valida")
            flag=True
def binario():
    flag=True
    while(flag):
        system("cls")
        print("--------------------------------------------Convertir desde Binario a ???---------------------------------------")
        print("")
        print("\t\t\t¿A que base quieres convertir?\t\t\t")
        print("\t\t\t1. Decimal")
        print("\t\t\t2. Quinario")
        print("\t\t\t3. Hexadecimal")
        print("\t\t\t4. Octal")
        print("\t\t\t5. Regresar al menu")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------")
        opcion=str(input())
        if(opcion=='1'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Binario a Decimal--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Binario")
                if(bandr!=False):
                    system("cls")
                    print("-----------------------------------------Convertir desde Binario a Decimal--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Decimal es {binario2Dec(numero)}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            binario()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='2'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Binario a Quinario--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Binario")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Binario a Quinario--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Quinario es {Dec2quinario(binario2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            binario()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='3'):
            flag=True
            while(flag):
                system("cls")
                print("----------------------------------------Convertir desde Binario a Hexadecimal----------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Binario")
                if(bandr!=False):
                    system("cls")
                    print("-------------------------------------Convertir desde Binario a Hexadecimal-------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Hexadecimal es {Dec2hexadecimal(binario2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            binario()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='4'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Binario a Octal--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Binario")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Binario a Octal--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Octal es {Dec2octal(binario2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            binario()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='5'):
            print("Regresando al menu anterior")
            main()
        else:
            print("Opcion no valida")
            flag=True
def quinario():
    flag=True
    while(flag):
        system("cls")
        print("--------------------------------------------Convertir desde Quinario a ???---------------------------------------")
        print("")
        print("\t\t\t¿A que base quieres convertir?\t\t\t")
        print("\t\t\t1. Decimal")
        print("\t\t\t2. Binario")
        print("\t\t\t3. Hexadecimal")
        print("\t\t\t4. Octal")
        print("\t\t\t5. Regresar al menu")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------")
        opcion=str(input())
        if(opcion=='1'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Quinario a Decimal--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Quinario")
                if(bandr!=False):
                    system("cls")
                    print("-----------------------------------------Convertir desde Quinario a Decimal--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Decimal es {quinario2Dec(numero)}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            quinario()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='2'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Quinario a Binario--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Quinario")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Quinario a Binario--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Binario es {Dec2binario(quinario2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            quinario()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='3'):
            flag=True
            while(flag):
                system("cls")
                print("----------------------------------------Convertir desde Quinario a Hexadecimal----------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Quinario")
                if(bandr!=False):
                    system("cls")
                    print("-------------------------------------Convertir desde Quinario a Hexadecimal-------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Hexadecimal es {Dec2hexadecimal(quinario2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            quinario()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='4'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Quinario a Octal--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Quinario")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Quinario a Octal--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Octal es {Dec2octal(quinario2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            quinario()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='5'):
            print("Regresando al menu anterior")
            main()
        else:
            print("Opcion no valida")
            flag=True
def hexadecimal():
    flag=True
    while(flag):
        system("cls")
        print("--------------------------------------------Convertir desde Hexadecimal a ???---------------------------------------")
        print("")
        print("\t\t\t¿A que base quieres convertir?\t\t\t")
        print("\t\t\t1. Decimal")
        print("\t\t\t2. Quinario")
        print("\t\t\t3. Binario")
        print("\t\t\t4. Octal")
        print("\t\t\t5. Regresar al menu")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------")
        opcion=str(input())
        if(opcion=='1'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Hexadecimal a Decimal--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Hexadecimal")
                if(bandr!=False):
                    system("cls")
                    print("-----------------------------------------Convertir desde Hexadecimal a Decimal--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Decimal es {hexadecimal2Dec(numero)}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            hexadecimal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='2'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Hexadecimal a Quinario--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Hexadecimal")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Binario a Quinario--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Quinario es {Dec2quinario(hexadecimal2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            hexadecimal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='3'):
            flag=True
            while(flag):
                system("cls")
                print("----------------------------------------Convertir desde Hexadecimal a Binario----------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Hexadecimal")
                if(bandr!=False):
                    system("cls")
                    print("-------------------------------------Convertir desde Hexadecimal a Binario-------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Binario es {Dec2binario(hexadecimal2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            hexadecimal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='4'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Hexadecimal a Octal--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Hexadecimal")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Hexadecimal a Octal--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Octal es {Dec2octal(hexadecimal2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            hexadecimal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='5'):
            print("Regresando al menu anterior")
            main()
        else:
            print("Opcion no valida")
            flag=True
def octal():
    flag=True
    while(flag):
        system("cls")
        print("--------------------------------------------Convertir desde Octal a ???---------------------------------------")
        print("")
        print("\t\t\t¿A que base quieres convertir?\t\t\t")
        print("\t\t\t1. Decimal")
        print("\t\t\t2. Quinario")
        print("\t\t\t3. Hexadecimal")
        print("\t\t\t4. Binario")
        print("\t\t\t5. Regresar al menu")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------")
        opcion=str(input())
        if(opcion=='1'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Octal a Decimal--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Octal")
                if(bandr!=False):
                    system("cls")
                    print("-----------------------------------------Convertir desde Octal a Decimal--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Decimal es {octal2Dec(numero)}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            octal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='2'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Octal a Quinario--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Octal")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Octal a Quinario--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Quinario es {Dec2quinario(octal2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            octal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='3'):
            flag=True
            while(flag):
                system("cls")
                print("----------------------------------------Convertir desde Octal a Hexadecimal----------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Octal")
                if(bandr!=False):
                    system("cls")
                    print("-------------------------------------Convertir desde Octal a Hexadecimal-------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Hexadecimal es {Dec2hexadecimal(octal2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            octal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='4'):
            flag=True
            while(flag):
                system("cls")
                print("------------------------------------------Convertir desde Octal a Binario--------------------------------------")
                print("")
                print("¿Que numero quieres convertir?")
                print("")
                print("-----------------------------------------------------------------------------------------------------------------")
                numero=str(input())
                bandr=verificar(numero,"Octal")
                if(bandr!=False):
                    system("cls")
                    print("------------------------------------------Convertir desde Octal a Binario--------------------------------------")
                    print("")
                    print(f"El numero {numero} convertido a Octal es {Dec2binario(octal2Dec(numero))}")
                    print("")
                    print("¿Quieres convertir otro numero en esta base?")
                    print("1. Si")
                    print("2. No")
                    print("3. Salir")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    band=True
                    while(band):
                        otro=str(input())
                        if(otro=="1"):
                            break 
                        elif(otro=="2"):
                            octal()
                        elif(otro=="3"):
                            sys.exit()
                        else:
                            print("Opcion no Valida")
                            band=False
                else:
                    "Numero invalido"
                    flag=True
        elif(opcion=='5'):
            print("Regresando al menu anterior")
            main()
        else:
            print("Opcion no valida")
            flag=True

#Menu a traves de consola para solicitar al usuario el numero

def main():
    flag=True
    while(flag):
        system("cls")
        print("-----------------------------Programa que convierte numeros con las siguientes bases-----------------------------")
        print("")
        print("\t\t\t\tDecimal,Binario,Quinario,Octal y Hexadecimal\t")
        print("")
        print("-----------------------------------------------------Menú--------------------------------------------------------")
        print("")
        print("\t\t\t¿Desde que base quieres convertir?\t\t\t")
        print("\t\t\t1. Decimal")
        print("\t\t\t2. Binario")
        print("\t\t\t3. Quinario")
        print("\t\t\t4. Hexadecimal")
        print("\t\t\t5. Octal")
        print("\t\t\t6. Salir")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------")
        opcion=str(input())
        if(opcion=='1'):
            Decimal() 
        elif(opcion=='2'):
            binario()
        elif(opcion=='3'):
            quinario()
        elif(opcion=='4'):
            hexadecimal()
        elif(opcion=='5'):
            octal()
        elif(opcion=='6'):
            sys.exit()
        else:
            print("Opcion no valida")
            flag=True
main()
        
#Prueba decimal a base

#Dec2binario(20)
#Dec2quinario(259)
#Dec2hexadecimal(7000)
#Dec2octal(50)

#Prueba base a decimal
#binario2Dec("010100")
#quinario2Dec("2014")
#hexadecimal2Dec("01B58")
#octal2Dec(62)