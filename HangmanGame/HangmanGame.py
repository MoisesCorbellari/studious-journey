from time import sleep
from random import choice
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
instrucoes = '''      Jogo da Forca!

Instruções:
1. Você deve escolher um tema para o jogo.
2. Uma palavra relacionada ao tema será escolhida aleatoriamente.
3. Você terá 6 tentativas para adivinhar a palavra.
4. A cada rodada, insira uma letra do alfabeto para adivinhar a palavra.
5. Você não pode inserir a mesma letra mais de uma vez.
                    
                    Divirta-se e boa sorte!
'''
print(instrucoes)
sleep(15)
limpar_tela()
user = input('Escolha seu nick: ').strip().title()
print(f'.......... Bem-vindo ao Jogo da Forca, {user}! ..........')
def contagem_regressiva(t):
    print('Iniciando em...')
    sleep(0.7)
    for t in range(t, 0, -1):
        print(t)
        sleep(1)
contagem_regressiva(3)
print('''Escolha o tema:

        [1] Fruta
        [2] Animal
        [3] Humano
        [4] Casa
    ''')
while True:
    try:
        escolha = int(input('Opção: '))
        if escolha<1 or escolha>4:
            raise ValueError
        break
    except ValueError:
        print('Opção inválida! Tente novamente.')
if escolha == 1:
    tema = 'Fruta'
    palavra = ['banana', 'abacaxi', 'melao', 'maça', 'morango', 'laranja', 'mamao', 
               'abacate', 'caju', 'cacau', 'melancia', 'limao', 'goiaba', 'graviola', 'uva']
elif escolha == 2:
    tema = 'Animal'
    palavra = ['cachorro', 'cavalo', 'onça', 'coelho', 'orangotango', 'elefante', 
               'abelha', 'aranha', 'borboleta', 'baleia', 'camelo', 'castor', 'camundongo', 'capivara']
elif escolha == 3:
    tema = 'Humano'
    palavra = ['cerebro', 'perna', 'braço', 'esqueleto', 'musculo', 'boca', 
               'intestino', 'medula', 'pele', 'bexiga', 'coraçao', 'rins', 'pulmao', 'coluna']
elif escolha == 4:
    tema = 'Casa'
    palavra = ['telhado', 'portao', 'janela', 'piso', 'chuveiro', 'vaso', 'panela', 
               'frigideira', 'travesseiro', 'toalha', 'mesa', 'copo', 'guardanapo', 'almofada']
escolhida = choice(palavra).upper()
tentativas = 6
letra_correta = []
letra_incorreta = []
while tentativas > 0:
    letra = input('Insira uma letra: ').upper().strip()
    if len(letra) != 1 or not letra.isalpha():
        print('Insira somente uma letra')
        continue
    if letra in letra_correta or letra in letra_incorreta:
        print('Você já tentou essa letra')
        continue
    if letra in escolhida:
        letra_correta.append(letra)
    else:
        letra_incorreta.append(letra)
        tentativas -= 1
    palavra_descoberta = ''
    for letra_palavra in escolhida:
        if letra_palavra in letra_correta:
            palavra_descoberta += letra_palavra
        else:
            palavra_descoberta += '_ '
    print('Palavra descoberta: ', palavra_descoberta)
    print('Letras corretas: ', ', '.join(letra_correta))
    print('Letras incorretas: ', ', '.join(letra_incorreta))
    print('Você tem {} tentativa(s) restante(s).'.format(tentativas))
    if palavra_descoberta == escolhida:
        print('Parabéns! Você acertou a palavra:', escolhida)
        jogar_novamente = input('Deseja jogar novamente? ("S" para continuar ou "N" para sair): ').strip().upper()
        if jogar_novamente == 'N' or jogar_novamente == 'n':
            print('\nObrigado por jogar! Até mais.\n')
            break
        if jogar_novamente == 'S' or jogar_novamente == 's':
            letra_correta = []
            letra_incorreta = []
            escolhida = choice(palavra).upper()
            tentativas = 6
            limpar_tela()
if tentativas == 0:
    print('GAME OVER! A palavra era:', escolhida)
