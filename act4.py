menu = """
 1 Número positivo, negativo o cero
 2 Número par o impar
 3 Evaluación de notas
 4 Clasificación por edad
 5 Tarifas de transporte
"""
print (menu)
opc=int(input("seleccione un numero: "))
if opc == 1:
    numero=int(input("deme un numero entero: "))
    if numero > 0:
        print(f"el numero {numero} es positivo")
    elif numero < 0:
        print(f"el numero {numero} es negativo")
    else:
        print (f"el numero {numero} es cero") 
elif opc == 2:
    numero = int(input("deme un numero entero: "))
    if numero % 2 == 0:
        print(f"el numero {numero} es par")
    else:
        print(f"el numero {numero} es impar")   
elif opc == 3:
    nota=float(input("rejistrar una nota de 0 a 5 : "))
    if nota >= 4.5:
        print(f"{nota} la nota es excelente")
    elif nota > 3.0:
        print(f"{nota} aprobo")
    else:
        print(f"{nota} reprobo")    
elif opc == 4:
    edad = int(input("deme su edad: "))
    if edad < 12:
        print(f" {edad} es niño")
    elif edad < 18:
        print(f" {edad} es adolecente")
    elif edad < 60:
        print(f" {edad} es adulto")
    else: 
        print(f"{edad} es adulto mayor")    
elif opc == 5:
    edad = int(input("deme su edad: "))
    if edad < 5:
        print(f"{edad} pasan gratis")
    elif edad < 12:
        print(f"{edad} Pagan tarifa infantil: $2.000")
    elif edad < 59:
        print(f"{edad} Pagan tarifa plena: $3.500")
    else:
        print("Pagan tarifa reducida: $2.500")  
else:
    print("lea socio")  


        
    
   



