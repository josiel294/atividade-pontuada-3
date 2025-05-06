import os
import time

os.system("clear || cls")


#Funções
def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09
    elif salario <= 4190.83:
        return salario * 0.12
    else:
        return salario * 0.14

def calcular_irrf(salario, dependentes):
    if salario <= 2259.20:
        return 0
    elif salario <= 2826.65:
        aliquota = 0.075
    elif salario <= 3751.05:
        aliquota = 0.15
    elif salario <= 4664.68:
        aliquota = 0.225
    else:
        aliquota = 0.275

    deducao = dependentes * 189.59
    desconto = (salario * aliquota) - deducao
    return max(0, desconto)

def calcular_vale_transporte(salario, opcao):
    return salario * 0.06 if opcao == "s" else 0

def calcular_vale_refeicao(valor):
    return valor * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150

# Acesso a conta do usuario
usuario_correto = "Rogerio"
senha_correta = "rogerio123"


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

import os
os.system ("clear || cls")

time.sleep(1)
print("\nLogin realizado com sucesso!\n")

# Entradas do usuario
salario = float(input("Informe o salário bruto: "))
vale_transporte = input("Deseja vale transporte? (s/n): ").lower()
valor_refeicao = float(input("Informe o valor mensal do vale-refeição: "))
dependentes = int(input("Quantos dependentes você possui: "))

# Cálculos
inss = calcular_inss(salario)
irrf = calcular_irrf(salario, dependentes)
transporte = calcular_vale_transporte(salario, vale_transporte)
refeicao = calcular_vale_refeicao(valor_refeicao)
plano_saude = calcular_plano_saude(dependentes)

# Total de descontos sobre o salário bruto
total_descontos_salario = inss + irrf + transporte + refeicao
salario_liquido = salario - total_descontos_salario

# Saída
print("\n--- Descontos ---")
print(f"INSS: R${inss:.2f}")
print(f"IRRF: R${irrf:.2f}")
print(f"Vale Transporte: R${transporte:.2f}")
print(f"Vale Refeição: R${refeicao:.2f}")
print(f"\nTotal de Descontos sobre o Salário: R${total_descontos_salario:.2f}")
print(f"Salário Líquido (sem plano de saúde): R${salario_liquido:.2f}")
print(f"Plano de Saúde (pago à parte): R${plano_saude:.2f}")
