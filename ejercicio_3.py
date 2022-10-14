peso=input("Cuál es tu peso? (Kg)")
estatura=input("Cuál es tu estatura? (metros)")
a=float(peso)
b=float(estatura)
imc=a/b**2
print("Tu IMC és:")
print(round(imc,2))
