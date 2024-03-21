import math
print("1.")
número = float(input("Insira um número."))
print("O antecessor é", número-1, "e o sucessor é", número +1)
print("2.")
número1 = float(input("Insira um número."))
número2 = float(input("Insira outro número."))
print("A soma dos números é", número1+número2)
print("3.")
número1 = float(input("Insira um número."))
número2 = float(input("Insira outro número."))
número3 = float(input("Insira outro número."))
print("A multiplicação dos números é", número1*número2*número3)
print("4.")
nota1 = float(input("Insira a nota do primeiro bimestre."))
nota2 = float(input("Insira a nota do segundo bimestre."))
nota3 = float(input("Insira a nota de terceiro bimestre."))
nota4 = float(input("Insira a nota do quarto bimestre."))
print("Sua média é:",(nota1+nota2+nota3+nota4)/4)
print("5.")
metros = float(input("Metros:"))
print(metros*100," centímetros")
print("6.")
# A=π r²
import math
raio = float(input("Insira o raio do círculo."))
print("A área do círculo é", (math.pow(raio,2))*math.pi)
print("7.")
import math
lado = float(input("Insira o lado do quadrado."))
print("A área do quadrado é", math.pow(lado,2))
print("O perímetro do quadrado é",lado*4)
print("8.")
salárioHora = float(input("Insira o salário por hora."))
hora = float(input("Insira as horas trabalhadas por dia."))
print("Você recebe", salárioHora*hora, "por dia.")
print("Você recebe", salárioHora*hora*30, "por 30 dias úteis.")
print("9.")
grausC = float(input("Quantos graus celsius?"))
print(grausC*9/5+32, "graus fahre")
print("10.")
import math
altura = float(input("Insira a sua altura."))
peso = float(input("Insira o seu peso."))
print("Seu IMC é:", peso/(math.pow(altura,2)))
print("11.")
import math
a = float(input("Insira o valor de a."))
b = float(input("Insira o valor de b."))
c = float(input("Insira o valor de c."))
delta = math.pow(b, 2)+(-4*a*c)
print(delta)
if (delta < 0):
    print("Delta é negativo, não há resultado real.")
if (delta == 0):
    print("Delta = 0, há apenas um resultado para x.")
    x = (-b + math.sqrt(delta))/(2*a)
    print(x)
else :
    x1 = (-b + math.sqrt(delta))/(2*a)
    print(round(x1,2))
    x2 = (-b - math.sqrt(delta))/(2*a) 
    print(round(x2,2))
print("12.")
nome = str(input("Insira o nome do produto: "))
valor = float(input("Insira o valor do produto: "))
porcentagem = int(input("Insira a porcentagem de desconto: "))
print("Produto:", nome)
print("Valor: R$", valor)
desconto = valor * (porcentagem /100)
print("Desconto: R$", desconto)
print("Valor final: R$", valor - desconto)
print("13.")
areaPintada = float(input("Quantos metros quadrados serão pintados?"))
qtndLitros = areaPintada /3
latasTinta = qtndLitros /18
if (qtndLitros%18 >0):
    latasTinta = latasTinta + 1
print("Será necessário",int(latasTinta), "latas de tinta e o preço total será R$", int(latasTinta) * 120.00)
print("14.")
salaHora = float(input("Quanto você recebe por hora?"))
horasTrab = int(input("Quantas horas você trabalha por mês?"))
salárioBruto = salaHora * horasTrab
impRenda = salárioBruto * 0.075
inss = salárioBruto * 0.08
sindicato = salárioBruto * 0.01
salárioLíquido = salárioBruto - impRenda -inss -sindicato
print("+ Salário bruto: R$", salárioBruto)
print("- IR (7.5%): R$", impRenda)
print("- INSS (8%): R$", inss)
print("- Sindicato: R$", sindicato)
print("= Salário Líquido: R$", salárioLíquido)