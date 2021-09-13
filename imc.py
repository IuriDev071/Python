peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# Calculando o IMC
imc = peso / altura ** 2

# Limitando o resultado para ter somente 1 casa decimal
imcDec = round(imc, 1)

if imcDec >= 18.6 and imcDec <= 25 :
    print("Seu IMC é: ",imcDec,"\nVocê está com o peso ideal")

elif imcDec <= 18.5 and imcDec > 17 :
    print("Seu IMC é: ",imcDec,"\nVocê está abaixo do peso ideal")

elif imcDec >= 25.1 and imcDec < 29.9 :
    print("Seu IMC é: ",imcDec,"\nVocê está com sobrepeso")

elif imcDec >= 30 and imcDec < 35  :
    print("Seu IMC é: ",imcDec,"\nVocê está com obesidade grau 1")

elif imcDec >= 36 and imcDec < 40 :
    print("Seu IMC é: ",imcDec,"\nVocê está com obesidade grau 2")

elif imcDec < 17 :
    print("Seu IMC é: ",imcDec,"\nVocê está com magreza grave")