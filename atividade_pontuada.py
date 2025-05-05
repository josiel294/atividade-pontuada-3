import os
os.system("cls" if os.name == "nt" else "clear")

import time

def calcular_inss(salario_bruto):
    if salario_bruto <= 1518.00:
        aliquota = 0.075
    elif salario_bruto <= 2793.88:
        aliquota = 0.09
    elif salario_bruto <= 4190.83:
        aliquota = 0.12
    else:
        aliquota = 0.14

    desconto_inss = salario_bruto * aliquota
    return desconto_inss

def calcular_irrf(salario_bruto):
    if 2259.21 <= salario_bruto <= 2826.65:
        aliquota = 0.075
    elif salario_bruto <= 3751.05:
        aliquota = 0.15
    elif salario_bruto <= 4664.68:
        aliquota = 0.225
    else:
        aliquota = 0.275

    desconto_irrf = (salario_bruto * aliquota) - (ndependentes * quantidade_dependentes)
    return desconto_irrf

def calcular_transporte (salario_bruto):
    if vale_transporte == "s":
        desconto_transporte = salario_bruto * 0.06
    else: 
        vale_transporte == "n"

    return desconto_transporte

def calcular_refeicao(valor_refeicao):
    valor_total_vale = valor_refeicao * 0.20
    return valor_total_vale

def calcular_dependente(dependentes):
    if dependentes == "s":
        numer
        


# Autenticação
usuario_correto = "Rogerio"
senha_correta = "rogerio123"
valor_dependente = 189.59
quantidade_dependentes = 0
valor_refeicao = 500
while True:
    usuario = input("Digite o usuário: ")
    if usuario == usuario_correto:
        break
    print("Usuário incorreto.\n")

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        break
    print("Senha incorreta.\n")


time.sleep(1)
print("\nLogin realizado com sucesso!\n")

# Entrada de dados
salario_bruto = float(input("Informe o salário bruto: "))
vale_transporte = input("Deseja vale transporte? (s/n): ").lower()
dependentes = int(input("Quantos dependentes você possui (0-10): "))
dependentes += quantidade_dependentes
# Cálculos
valor_inss = calcular_inss(salario_bruto)
valor_irrf = calcular_irrf(salario_bruto)
valor_transporte = calcular_transporte(salario_bruto)

print(f"\nO valor do desconto do INSS é: R${valor_inss:.2f}")
print(f"O valor do desconto do IRRF é: R${valor_irrf:.2f}")
print(f"O valor do desconto do vale transporte é: R${valor_transporte:.2f}")

# Verificação de vale-transporte
if vale_transporte == "s":
    print("Você optou por Vale Transporte.")
elif vale_transporte == "n":
    print("Você não optou por Vale Transporte.")
else:
    print("Opção inválida para Vale Transporte.")
