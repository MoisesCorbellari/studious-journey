from time import sleep
from tqdm import tqdm
from random import choice
import string
dig_pass = int(input('Informe o número de digítos da senha que deseja: '))
for i in tqdm(range(0, 100), desc='GERANDO SENHA'): sleep(.0130)
caracteres = string.ascii_letters + string.digits + string.punctuation
seguranca = ' '
for i in range(dig_pass):
    seguranca += choice(caracteres)
print('Senha gerada: ', seguranca)
