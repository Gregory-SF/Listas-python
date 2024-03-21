print("1.")
num = float(input("Insira um número:"))
if(num == 0):
    print("O número é não nulo")
else:
    if (num>0):
        print("O número é positivo.")
    else:
        print("O número é negativo.")     

print("2.")
num1 = int(input("Insira um número:"))
num2 = int(input("Insira um número:"))
if (num1 > num2):
    print(num1)
else:
    print(num2)

print("3.")
idade = int(input("Insira sua idade:"))
if (idade > 18):
    print("Entrada permitida")
else:
    print("Entrada negada")

print("4.")
notaTrab = float(input("Insira a nota do trabalho."))
notaProva = float(input("Insira a nota da prova."))
if((notaTrab+notaProva)/2 >= 60):
    print("Aprovado")
else:
    print("Reprovado")

print("5.")
conceito = input("Insira seu conceito.")
if(conceito == "D"):
    print("Reprovado")
else:
    if(conceito == "C"):
        print("Aprovado")
    else:
        if(conceito == "B"):
            print("Aprovado")
        else:
            if(conceito == "A"):
                print("Aprovado")
            else:
                print("Conceito inválido")

print("6.")
salario = float(input("Insira seu salário:"))
if (salario < 1212):
    print("Você recebe menos que um sálario mínimo")
else:
    print("Você rebece aproximadamente", int(salario//1212), "salários mínimos.")

print("7.")
sexo = input("Insira seu sexo: F ou M. ")
if (sexo == "F"):
   print("Feminino")
else:
    if(sexo == "M"):
        print("Masculino")
    else:
        print("Sexo inválido")

print("8.")
idade = int(input("Insira sua idade. "))
if (idade >= 18):
    nome = input("Insira seu nome.")
    print("Bem vindo,", nome)
else:
    print("Entrada não permitida.")

print("9.")
idade = int(input("Insira sua idade. "))
if (idade >= 18):
    salario = float(input("Insira seu saláro."))
    print("Saláro final: R$", salario*1.05)
else:
    print("Cálculo não permitido.")

print("10.")
numero = int(input("Insira um número: "))
if(numero>0):
    if (numero < 100):
        print("Número no intervalo definido.")
    else:
        print("Número fora do intervalo!")
else:
    print("Número fora do intervalo!") 

print("11.")
valor = int(input("Insira um número. "))
if (valor%2 ==0):
    print("O número", valor, "é par.")
else:
    print("O número", valor, "é ímpar.")

print("12.")
valor = int(input("Insira um número. "))
if (valor%3 ==0):
    print("O número", valor, "é múltiplo de 3.")
else:
    print("O número", valor, "não é múltiplo de 3.")

print("13.")
a = float(input("Insira um valor para A. "))
b = float(input("Insira um valor para B. "))
c = float(input("Insira um valor para C. "))
if (a+b > c):
    print("A+B é maior que C.")
else:
    print("C é maior que todos!")

print("14.")
valor = int(input("Insira um número inteiro. "))
if (valor%2 ==0):
    print(valor+5)
else:
    print(valor*2)

print("15.")
valor = int(input("Insira um númere inteiro. "))
if (valor<0):
    valor = int(input("Insira um númere inteiro. "))
print(valor*10)

print("16.")
valor = int(input("Insira um número inteiro. "))
if(valor>0):
    if (valor%2 ==0):
        print("Par.")
    else:
        print("Ímpar.")
else:
    print(valor+100)

print("17.")
preco = float(input("Insira a o valor da compra. "))
if (preco > 100):
    desconto = (10/100) * preco
    print("Desconto: R$", desconto)
    preco = preco - desconto
print("Preço: R$", preco)

print("18.")
preco = float(input("Insira a o valor da compra. "))
if (preco > 500):
    pagamento = input("Insira a forma de pagamento: PIX ou outras opções.")
    if (pagamento == "PIX"):
        desconto = (10/100) * preco
    else:
        desconto = (5/100) * preco
else:
    pagamento = input("Insira a forma de pagamento: PIX ou outras opções.")
    if (pagamento == "PIX"):
        desconto = (5/100) * preco
    else:
        desconto = 0
print("Desconto: R$", desconto)
preco = preco - desconto
print("Preço: R$", preco)

print("19.")
salario = float(input("Insira seu salário: R$"))
if (salario >= 2826.65):
    desconto = 15/100 * salario
else:
    if(salario>1903.98):
        desconto = 7.5/100 * salario
    else:
        desconto = 0.0
print("Você deverá pagar R$", desconto)

print("20.")
x = int(input("Insira o valor de x. "))
if(x == 2):
    print("Resultado inexistente!")
else:
    if (x<2):
        resultado = 1/(2-x)
    else: 
        resultado = 1/(x-2)
    print("f(x) =", resultado)

print("21.")
a = float(input("Insira um valor para A. "))
b = float(input("Insira um valor para B. "))
c = float(input("Insira um valor para C. "))
# if(a>b):
#     if(a>c):
#         print(a)
#     else:
#         print(c)
# elif (a>c):
#     print(b)
# else:
#     if(b>c):
#         print(b)
#     else:
#         print(c)
if (a>b):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)

print("22.")
a = float(input("Insira um valor. "))
b = float(input("Insira um valor. "))
c = float(input("Insira um valor. "))
d = float(input("Insira um valor. "))
if (a>b):
    if(a>c):
        if(a>d):
            print(a)
        else:
            print(d)
    else:
        if(c>d):
            print(c)
        else:
            print(d)
    print(b)
else:
    if(b>c):
        if(b>d):
            print(b)
        else:
            print(d)
    else:
        if(c>d):
            print(c)
        else:
            print(d)
    print(a)