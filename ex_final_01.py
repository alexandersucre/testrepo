a = int(input("Introduzca el primer número: "))
b = int(input("Introduzca el segundo número: "))
if a!=0 and b!=0:
    if a%2==0 and b%2==0:
        c = a + b
        print(f"El resultado es: {c}")
    else:
        print("Alguno de los número no es par.")
else:
    print("Alguno de los número es 0.")
    