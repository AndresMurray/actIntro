numeros = [] 
while True:
    num= input("ingrese un numero o escriba fin para finalizar")
    if num == "fin":
        break
    else:
        numero=int(num)
        numeros.append(numero)
print("la lista de numeros ingresados es:")
for i in numeros:
    if i < 0:
        break
    else:
        print(i)
        



        
    