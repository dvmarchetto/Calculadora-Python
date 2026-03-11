nome = input("Digite o nome do estudante: ")

soma_notas = 0
quantidade_trimestre = 3
meta_aprovação = 180

for i in range(1, quantidade_trimestre + 1):
    nota = float(input(f"Informe a nota do {i}º período "))
    soma_notas += nota

print ("-" * 30)
print (f"estudante: {nome}")
print (f"pontuação total: {soma_notas}")

if soma_notas >= meta_aprovação:
    print("Status: Aprovado! Muito bem!")
else:
    pontos_faltantes = meta_aprovação - soma_notas
    print ("Status: Reprovou! Tente novamente ano que vem!")
    print(f"Faltaram {pontos_faltantes} pontos para atingir o mínimo de {meta_aprovação}")