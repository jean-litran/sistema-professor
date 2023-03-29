print("""
Bem vindo ao Sistema professor 1.0
feito por Saruman sem chat gpt
 _____                 _             
/  __ \               | |            
| /  \/ ___  _ __ ___| |_ ___  _ __ 
| |    / _ \| '__/ __| __/ _ \| '__|
| \__/\ (_) | |  \__ \ || (_) | |   
 \____/\___/|_|  |___/\__\___/|_|   
""")

# Função para inserir notas de um aluno
def inserir_notas_aluno():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    media = (nota1 + nota2) / 2
    print(f"A média do aluno {nome} é {media}\n")
    return media

# Função para calcular a média da turma
def calcular_media_turma(turma):
    media_turma = sum(turma) / len(turma)
    return media_turma

# Lista para armazenar as notas da turma A
turma_a = []

# Lista para armazenar as notas da turma B
turma_b = []

# Loop para inserir as notas dos alunos
while True:
    print("1. Inserir nota da turma A")
    print("2. Inserir nota da turma B")
    print("3. Calcular média das turmas")
    print("4. Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        nota_a = inserir_notas_aluno()
        turma_a.append(nota_a)
    elif opcao == 2:
        nota_b = inserir_notas_aluno()
        turma_b.append(nota_b)
    elif opcao == 3:
        media_a = calcular_media_turma(turma_a)
        media_b = calcular_media_turma(turma_b)
        print(f"Média da turma A: {media_a}")
        print(f"Média da turma B: {media_b}")
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Tente novamente.\n")
def salvar_medias(media_a, media_b, turma_a, turma_b, nome_arquivo):
    with open(f"{nome_arquivo}.txt", "w") as arquivo:
        arquivo.write(f"Média da turma A: {media_a}\n")
        arquivo.write(f"Média da turma B: {media_b}\n\n")
        arquivo.write("Turma A:\n")
        for i, nota in enumerate(turma_a):
            nome = input(f"Digite o nome do aluno {i+1} da turma A: ")
            arquivo.write(f"{nome}: {nota}\n")
        arquivo.write("\nTurma B:\n")
        for i, nota in enumerate(turma_b):
            nome = input(f"Digite o nome do aluno {i+1} da turma B: ")
            arquivo.write(f"{nome}: {nota}\n") 
# salvar as médias da turma A e B no arquivo "medias.txt"
salvar_medias(media_a, media_b, turma_a, turma_b, "medias")

print("Arquivo medias.txt salvo com sucesso!")

#feito por saruman sem chat gpt
