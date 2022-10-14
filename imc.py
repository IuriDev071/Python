peso_imc = int(input("Qual seu peso ?"))
altura_imc = float(input("Qual sua altura ?"))
imc = peso_imc / (altura_imc * altura_imc)
roundImc = round(imc, 1)

if roundImc <= 18.5:
    print("Magreza")
elif roundImc <= 24.9 and roundImc <= 18.6:
    print("Normal")
elif roundImc <= 25 and roundImc <= 29.9:
    print("Sobrepeso")
elif roundImc <= 34.9 and roundImc <= 30:
    print("Obesidade grau 1")
elif roundImc <= 35 and roundImc <= 39.9:
    print("Obesidade grau 2")
elif roundImc <= 40 and roundImc <= 49.9:
    print("Obesidade grau 3")
else:
    print("Erro, preencha as informações corretamente!")