from time import sleep
from random import choice
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
sleep(6)

usuario = input('Escolha seu nick: ').strip()
print('.......... Bem-vindo ao Jogo da Forca, {}! ..........'.format(usuario))
input('Pressione ENTER para jogar!')

def contagem_regressiva(segundos):
    for t in range(segundos, 0, -1):
        print('Iniciando em {}'.format(t))
        sleep(1)

contagem_regressiva(3)

print('''Escolha o tema:

        [1] Fruta
        [2] Animal
        [3] Humano
        [4] Casa
    ''')

escolha = int(input('Opção: '))

if escolha == 1:
    tema = 'Fruta'
    palavra = ['Banana', 'Abacaxi', 'Melão', 'Maçã', 'Morango', 'Laranja']
elif escolha == 2:
    tema = 'Animal'
    palavra = ['Cachorro', 'Cavalo', 'Onça', 'Coelho', 'Orangotango', 'Elefante']
elif escolha == 3:
    tema = 'Humano'
    palavra = ['Cérebro', 'Perna', 'Braço', 'Esqueleto', 'Músculo', 'Boca']
elif escolha == 4:
    tema = 'Casa'
    palavra = ['Telhado', 'Portão', 'Janela', 'Piso', 'Chuveiro', 'Vaso']
else:
    print('Opção Inválida! Escolha uma das opções para o tema do jogo.')

escolhida = choice(palavra).upper()

tentativas = 6
letra_correta = []
letra_incorreta = []

while tentativas > 0:
    letra = input('Insira uma letra: ').upper().strip()

    if len(letra) != 1 or not letra.isalpha():
        print('Insira somente uma letra.')
        continue

    if letra in letra_correta or letra in letra_incorreta:
        print('Você já tentou essa letra.')
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
        jogar_novamente = input('Deseja jogar novamente? (S para Sim e N para Não): ').strip().upper()
        if jogar_novamente == 'S':
            letra_correta = []
            letra_incorreta = []
            escolhida = choice(palavra).upper()
            tentativas = 6
        else:
            break

if tentativas == 0:
    print('GAME OVER! A palavra era:', escolhida)
