#---------------------------------------------------------------------
# Este programa faz jogos SURPRESINHA para a LotoFacil da Caixa
#---------------------------------------------------------------------

from random import randrange

numero_de_jogos = int(input('Digite a Quantidade de Supresinhas Desejada: '))

# Abre o arquivo para escrita
with open('Surpresinha LotoFacil.txt', 'w') as arquivo:
    # Gera a quantidade de jogos informada com 15 números únicos cada jogo
    indice = 1
    while indice < (numero_de_jogos + 1):
        # Cria um conjunto para armazenar números únicos para cada jogo
        numeros_unicos = set()

        # Gera 15 números únicos para o jogo atual
        while len(numeros_unicos) < 15:
            numeros_unicos.add(randrange(1, 26))
        
        # Converte o conjunto para uma lista e classifica
        lista_classificada = sorted(numeros_unicos)
        
        # Converte a lista em uma string formatada
        if indice < 10:
            strindice = '0' + str(indice)
        else:
            strindice = str(indice)
            
        linha = 'Jogo ' + strindice + '  = ' + ', '.join(map(str, lista_classificada)) + '\n'
        
        # Escreve a linha no arquivo
        arquivo.write(linha)
        
        # Incrementa o índice
        indice += 1

print("Os Jogos Foram Salvos no arquivo Surpresinha LotoFacil.txt'.")
