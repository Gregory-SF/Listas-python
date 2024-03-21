# print("1.")
# import math
# import random
# import sys
# print("== Menu de Opções ==")
# print("1. Somar 2 números")
# print("2. Potência Y de um número X (x^y)")
# print("3. Raiz quadrada de X")
# print("4. Gerar um número aleatório")
# escolha = int(input("== Opção escolhida:"))
# if(escolha == 1):
#     x = float(input("Insira um valor. "))
#     y = float(input("Insira outro valor. "))
#     print(x, "+", y, "=", x+y)
# elif(escolha == 2):
#     x = float(input("Insira um valor. "))
#     y = float(input("Insira outro valor. "))
#     print("Potência", y, "de um número", x, math.pow(x,y))
# elif(escolha == 3):
#     x = float(input("Insira um valor. "))
#     print("Raíz quadrada de", x, "é:", math.sqrt(x))
# elif(escolha == 4):
#     x = sys.maxsize
#     y = sys.maxsize * -1 
#     print(random.randint(y,x))
# else:
#     print("Opção inválida.")

# print("2.")
# peso = float(input("Insira seu peso. "))
# altura = float(input("Insira seu altura. "))
# IMC = peso / math.pow(altura,2)
# if(IMC<18.5):
#     print("Baixo peso")
# elif(IMC<24.9):
#     print("Peso normal")
# elif(IMC<29.9):
#     print("Pré-obesidade")
# elif(IMC<34.9):
#     print("Obesidade Grau I")
# elif(IMC<39.9):
#     print("Obesidade Grau II")
# else:
#     print("Obesidade Grau III")

# print("3.")
# salarioAntigo = float(input("Insira seu salário. "))
# if(salarioAntigo <= 710.00):
#     aumento = 20/100
#     salarioNovo = salarioAntigo + salarioAntigo * aumento
# elif(salarioAntigo <= 1000.00):
#     aumento = 15/100
#     salarioNovo = salarioAntigo + salarioAntigo * aumento
# elif(salarioAntigo <= 2500.00):
#     aumento = 10/100
#     salarioNovo = salarioAntigo + salarioAntigo * aumento
# else:
#     aumento = 5/100
#     salarioNovo = salarioAntigo + salarioAntigo * aumento
# print("Salário antes do reajuste: R$", salarioAntigo)
# print("Aumento de", int(aumento * 100), "%")
# print("Valor do aumento: RS", aumento * salarioAntigo)
# print("Novo salário: R$", salarioNovo)

# print("4.")
# import math
# import random
# print("== Menu de Opções ==")
# print("1. Gerar um número aleatório entre X e Y")
# print("2. X é par pu ímpar?")
# print("3. Valor R$X com Y% de desconto")
# escolha = int(input("== Opção escolhida:"))
# if(escolha == 1):
#     x = int(input("Insira um valor mínimo. "))
#     y = int(input("Insira um valor máximo. "))
#     print(random.randint(x,y))
# elif(escolha == 2):
#     x = int(input("Insira um valor para x. "))
#     if(x%2 != 0):
#         print("O número", x, "é impar.")
#     else:
#         print("O número", x, "é par.")
# elif(escolha == 3):
#     x = float(input("Insira um valor para x. "))
#     y = int(input("Insira um valor para y. "))
#     print("O valor R${} com {}% de desconto fica R${}".format(x,y,x - x * (y/100)))
# else:
#     print("Opção inválida.")

# print("5.")
# sus = 0
# if(input("Telefonou para a vítima? ").lower() == "sim"):
#     sus = sus + 1
# if(input("Esteve no locak do crime? ").lower() == "sim"):
#     sus = sus + 1
# if(input("Mora perto da vítima? ").lower() == "sim"):
#     sus = sus + 1
# if(input("Devia para a vítima? ").lower() == "sim"):
#     sus = sus + 1
# if(input("Ja trabalhou com a vítima? ").lower() == "sim"):
#     sus = sus + 1
# if(sus<2):
#     print("Inocente")
# elif(sus<3):
#     print("Suspeita")
# elif(sus<5):
#     print("Cúmplice")
# else:
#     print("Assasino")

# print("6.")
# salarioAntigo = float(input("Insira seu salário. "))
# if(salarioAntigo <= 280.00):
#     aumento = 20/100
#     salarioNovo = salarioAntigo + salarioAntigo * aumento
# elif(salarioAntigo <= 700.00):
#     aumento = 15/100
#     salarioNovo = salarioAntigo + salarioAntigo * aumento
# elif(salarioAntigo <= 1500.00):
#     aumento = 10/100
#     salarioNovo = salarioAntigo + salarioAntigo * aumento
# else:
#     aumento = 5/100
#     salarioNovo = salarioAntigo + salarioAntigo * aumento
# print("Salário antes do reajuste: R$", salarioAntigo)
# print("Aumento de", int(aumento * 100), "%")
# print("Valor do aumento: RS", aumento * salarioAntigo)
# print("Novo salário: R$", salarioNovo)

# print("7.")
# mes = int(input("Insira o número do mês. "))
# if(mes == 2):
#     print("28 dias")
# elif(mes <= 7):
#     if(mes%2 == 0):
#         print("30 dias")
#     else:
#         print("31 dias")
# else:
#     if(mes%2 == 0):
#         print("31 dias")
#     else:
#         print("30 dias")

# print("8.")
# x = float(input("Insira um número. "))
# calculo = input("Insira o cálculo desejado. ")
# y = float(input("Insira um número. "))
# if(calculo == "+"):
#     resultado = x + y
#     print("=", resultado)
# elif(calculo == "-"):
#     resultado = x - y
#     print("=", resultado)
# elif(calculo == "x"):
#     resultado = x * y
#     print("=", resultado)
# elif(calculo == "/"):
#     resultado = x / y
#     print("=", resultado)
# else:
#     print("Erro.")

# print("9.")
# combustivel = input("Insira G para gasolina ou A para álcool. ")
# if(combustivel == "G"):
#     preco = 5.49
#     litros = int(input("Insira a quantidade de litros. "))
#     if(litros<=20):
#         valor = litros * (preco - preco * (3/100))
#     else:
#         valor = litros * (preco - preco * (5/100))
#     print("Valor a ser pago: R$", valor)
# elif(combustivel == "A"):
#     preco = 3.99
#     litros = int(input("Insira a quantidade de litros. "))
#     if(litros<=20):
#         valor = litros * (preco - preco * (4/100))
#     else:
#         valor = litros * (preco - preco * (6/100))
#     print("Valor a ser pago: R$", valor)
# else:
#     print("Erro.")

print("10.")