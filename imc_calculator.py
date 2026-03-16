# #CALCULADORA DE IMC
#peso/altura*altura=BMI
print("Calculadora de IMC")
Peso = float(input("Digite seu peso em KG: "))
Altura = float(input("Digite sua altura em metros: "))
imc = Peso / (Altura * Altura)
print(f"Seu IMC é: {int(imc)}")
if imc >= 35:
    print("Obesidade Mórbida")
elif imc >= 30: 
    print("Obesidade")
elif imc >= 25:
    print("Excesso de peso")
elif imc >= 18:
    print("Peso saudavel")
else:
    print("Extrema magreza")