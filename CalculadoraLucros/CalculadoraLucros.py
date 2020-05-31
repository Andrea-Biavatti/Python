print("Heitor Bisneto [Versão 1.0]")
print("(c) - 2019-2020 Bisneto Inc. Todos os direitos reservados")
print("")
print("*Calculadora de lucros*\n")
# Use somente números no campo. Não use vírgulas. Use Ponto final no lugar de vírgulas.
ValorTotal = float(input("<Valor Total do Produto> "))
# Use somente números. Não use sinal de porcentagem
Margem = float(input("<Margem de Lucro> "))
Calculo = (((ValorTotal/100)* Margem) + ValorTotal)

print("<Valor de Venda> R$", Calculo)
