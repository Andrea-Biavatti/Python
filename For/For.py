print("Heitor Bisneto [Versão 1.0]")
print("(c) - 2019 Bisneto Inc. Todos os direitos reservados")
print("")
#Laço For:
print("1. Laço FOR com a extensão de 10 números:")
print("")
for Contador in range(10):
    print(Contador)

#Laço For com número inicial e número final inserido pelo o usuário:
print("")
print("2. Laço FOR com a extensão predefinida de acordo com o usuário:")
InicialItem = int(input("Insira um número inicial: "))
Range = int(input("Insira um número final: "))
FinalItem = (Range + 1)
print("")

for Contador in range(InicialItem, FinalItem):
    print(Contador)

#Laço For com intervalos definidos pelo usuário:
print("")
print("3. Laço FOR com a extensão e intervalos predefinidos de acordo com o usuário:")
InicialItem = int(input("Insira um número inicial: "))
Range = int(input("Insira um número final: "))
Intervalo = int(input("Defina um intervalo entre os números: "))
FinalItem = (Range + 1)
print("")

for Contador in range(InicialItem, FinalItem, Intervalo):
    print(Contador)
