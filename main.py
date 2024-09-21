import random
import matplotlib.pyplot as plt
import pandas as pd
import time
from colorama import Fore, Back, Style, init
init()

def forca_opcao(lista_opcoes, msg, msg_erro): #Forçar o usuário a escolher uma opção
    opcao = input(msg)
    while opcao not in lista_opcoes:
        print(Fore.RED + "Opção inválida! Somente essas:\n" + Style.RESET_ALL + f"{msg_erro}")
        opcao = input(msg)
    return opcao

def tem_saldo(saldo, custo): #Verificar se o usuário ainda tem saldo suficiente
    if custo < saldo:
        return True
    print("Quantidade de créditos insuficente, escolha outra opção!")
    return False

def gerar_pontuacao():
    return random.randint(50, 100)

# Função para calcular a pontuação final do jogador
def calcular_pontuacao_final(escolhas):
    # Gerando pontuação para cada elemento
    pontuacao_total = 0
    print(Style.BRIGHT + "===== PONTUAÇÕES =====" + Style.RESET_ALL)
    for key in escolhas.keys():
        for indice in range(len(escolhas[key])):
            pontuacao = gerar_pontuacao()
            print(f"{escolhas[key][indice]}: {pontuacao} pontos")
            pontuacao_total += pontuacao

    return pontuacao_total

def ordenar_ranking(jogadores, pontuacoes):
    # Cria uma lista de pares (jogador, pontuação)
    ranking = []
    for i in range(len(jogadores)):
        ranking.append([jogadores[i], pontuacoes[i]])

    # Implementação do algoritmo Bubble Sort
    n = len(ranking)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Se a pontuação atual for menor que a próxima, troca as posições
            if ranking[j][1] < ranking[j + 1][1]:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

    return ranking

def gerar_ranking(jogador_pontuacao):
    jogadores_ficticios = ["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4", "Jogador 5"]
    pontuacoes_ficticias = []
    for _ in range(len(jogadores_ficticios)):
        pontuacoes_ficticias.append(random.randint(200, 350))

    # Incluindo a pontuação do jogador no ranking
    jogadores_ficticios.append(Fore.LIGHTCYAN_EX +"Você"+Style.RESET_ALL)
    pontuacoes_ficticias.append(jogador_pontuacao)

    # Ordenando o ranking pela pontuação
    ranking = ordenar_ranking(jogadores_ficticios, pontuacoes_ficticias)

    # Exibe o ranking ordenado
    print(Style.BRIGHT +"\nRanking final:"+ Style.RESET_ALL)
    for i in range(len(ranking)):
        print(Style.BRIGHT +f"{i + 1}."+ Style.RESET_ALL + f" {ranking[i][0]} - {ranking[i][1]} pontos")

    return ranking

def escolhendo_elemento(creditos, chave):
    while True:
        tabela = pd.DataFrame(escolhas_hitrace[chave])
        print(tabela)

        indices = []
        for i in range(len(escolhas_hitrace[chave]['nomes'])):
            indices.append(str(i))

        escolha = forca_opcao(indices,
                              "Escolha uma das opções (digite o número correspondente):\n-> ",
                              tabela)
        indice = int(escolha)
        if tem_saldo(creditos, escolhas_hitrace[chave]['precos'][indice]):
            elemento = escolhas_hitrace[chave]['nomes'][indice]
            escolhas_usuario[chave].append(elemento)
            preco = escolhas_hitrace[chave]['precos'][indice]
            creditos -= preco
            print(Fore.YELLOW +f"Você possui {creditos} créditos."+ Style.RESET_ALL)
            return [elemento, indice, preco, creditos]


escolhas_hitrace = {
    #Área de Pilotos
    "pilotos": {
        'nomes' : ["Mitch EVANS", "Antônio Felix DA COSTA", "Nyck DE VRIES"],
        'equipes' : ["Jaguar", "Porsche", "Mahindra"],
        'precos' : [17, 14, 9],
    },

    #Área de Equipes
    "equipes": {
        'nomes' : ["Porsche", "Jaguar", "Mahindra", "Maserati", "McLaren"],
        'precos' : [17, 15, 13, 12, 13],
    },

    #Área de Motores
    "motores": {
        'nomes' : ["Porsche 99X Electric", "Mahindra M9Electro", "Jaguar I-Type 6"],
        'precos' : [17, 11, 16],
    },

    #Área de Técnicos
    "técnicos": {
        'nomes' : ["Thomas Biermaier", "Frederic Bertrand", "Florian Modlinger"],
        'equipes' : ["ABT", "Mahindra", "Porsche"],
        'precos' : [11, 12, 18],
    }
}

print(Fore.BLUE + "====== Seja bem-vindo(a) ao HitRace Fantasy Formula E ======"+ Style.RESET_ALL)
nome_equipe = input("Digite um nome para a sua equipe:\n-> ")

creditos = 100
print(Fore.YELLOW +f"Você recebeu {creditos} créditos iniciais."+ Style.RESET_ALL)
escolhas_usuario = {
    "pilotos": [],
    "equipes": [],
    "motores": [],
    "técnicos": []
}
#O usuário é apresentado a lista de pilotos e a sua quantidade atual de créditos, ao escolher um piloto a
# quantidade de créditos é retirada do usuário, e caso escolha uma opção que não exista ele é forçado a responder
# corretamente, e se ele não tiver créditos suficientes, ele volta ao inicio do while. E por fim caso de certo, o piloto escolhido é removido.


print(Style.BRIGHT + "=== PILOTOS DISPONÍVEIS ==="+ Style.RESET_ALL)
escolha_piloto1 = escolhendo_elemento(creditos, 'pilotos')
piloto1 = escolha_piloto1[0]
indice1 = escolha_piloto1[1]
preco_piloto1 = escolha_piloto1[2]
creditos = escolha_piloto1[3]
for key in escolhas_hitrace['pilotos'].keys():
    escolhas_hitrace['pilotos'][key].remove(escolhas_hitrace['pilotos'][key][indice1])
print(f"Seu piloto 1 é o " + Style.BRIGHT + f"{piloto1}!\n" + Style.RESET_ALL)


print(Style.BRIGHT +"=== PILOTOS DISPONÍVEIS ==="+ Style.RESET_ALL)
escolha_piloto2 = escolhendo_elemento(creditos, 'pilotos')
piloto2 = escolha_piloto2[0]
preco_piloto2 = escolha_piloto2[2]
creditos = escolha_piloto2[3]
print(f"Seu piloto 2 é o " + Style.BRIGHT + f"{piloto2}!\n"+ Style.RESET_ALL)


print(Style.BRIGHT + "=== EQUIPES DISPONÍVEIS ==="+ Style.RESET_ALL)
escolha_equipe = escolhendo_elemento(creditos, 'equipes')
equipe = escolha_equipe[0]
preco_equipe = escolha_equipe[2]
creditos = escolha_equipe[3]
print(f"Sua equipe é a " + Style.BRIGHT + f"{equipe}!\n"+ Style.RESET_ALL)


print(Style.BRIGHT + "=== MOTORES DISPONÍVEIS ==="+ Style.RESET_ALL)
escolha_motor = escolhendo_elemento(creditos, 'motores')
motor = escolha_motor[0]
preco_motor = escolha_motor[2]
creditos = escolha_motor[3]
print(f"Seu motor é o " + Style.BRIGHT + f"{motor}!\n" + Style.RESET_ALL)


print(Style.BRIGHT + "=== TÉCNICOS DISPONÍVEIS ==="+ Style.RESET_ALL)
escolha_tecnico = escolhendo_elemento(creditos, 'técnicos')
tecnico = escolha_tecnico[0]
preco_tecnico = escolha_tecnico[2]
creditos = escolha_tecnico[3]
print(f"Sua equipe é a "+ Style.BRIGHT + f"{tecnico}!\n" + Style.RESET_ALL)


print(f"Sua equipe, a "+ Fore.BLUE +f"{nome_equipe}" + Style.RESET_ALL + ", está escalada assim:\n" #Um print mostrando todas as opções escolhidas pelo usuário
      # e sua quantidade final de créditos.
      + Style.BRIGHT +f"Piloto 1:" + Style.RESET_ALL + f"{piloto1} - {preco_piloto1} créditos\n"
      + Style.BRIGHT +f"Piloto 2:" + Style.RESET_ALL + f" {piloto2} - {preco_piloto2} créditos\n"
      + Style.BRIGHT +f"Equipe representante:" + Style.RESET_ALL + f" {equipe} - {preco_equipe} créditos\n"
      + Style.BRIGHT +f"Motor:" + Style.RESET_ALL + f" {motor} - {preco_motor} créditos\n"
      + Style.BRIGHT +f"Técnico:" + Style.RESET_ALL + f" {tecnico} - {preco_tecnico} créditos\n"
      + Fore.YELLOW +f"Seu saldo restante é de {creditos} créditos.\n"+ Style.RESET_ALL)

print("A corrida começou!!! Os resultados sairão em...")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

# Calcula a pontuação total baseada em desempenho
pontuacao_final = calcular_pontuacao_final(escolhas_usuario)
print(Fore.GREEN +f"\nPontuação total: {pontuacao_final} pontos"+ Style.RESET_ALL)

# Gerar e mostrar o ranking
ranking_final = gerar_ranking(pontuacao_final)

# Gráfico com matplotlib mostrando as escolhas e os créditos restantes
categorias = ['Piloto 1', 'Piloto 2', 'Equipe', 'Técnico', 'Motor']
custos = [preco_piloto1, preco_piloto2, preco_equipe, preco_tecnico, preco_motor]

plt.figure(figsize=(8, 6))
plt.bar(categorias, custos, color='royalblue')
plt.title('Créditos gastos por categoria')
plt.ylabel('Créditos')
plt.show()

