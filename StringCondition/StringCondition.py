from datetime import date
AnoAtual = date.today().year
SoftwareName = "STRINGCONDITION"

print("Nome:", SoftwareName)
print("Versão: 1.1")
print("Criado por: Heitor Bisneto")
print("Copyright © 2019 -", AnoAtual, "Bisneto. All rights reserved.")
print("")
Nome = str(input("Escreva algo usando letras: "))

if Nome == "Moqueca" or Nome == "moqueca":
    print("Categoria: Comida")
if Nome == "Ford" or Nome == "ford":
    print("Categoria: Marca de carro")
else:
    print("Categoria: Não Cadastrada")
