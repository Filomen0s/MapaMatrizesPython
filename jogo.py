import os
import time
import keyboard #pip install keyboard

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrarMapa(mapa):
    limpar_terminal()
    for linha in mapa:
        mapaVisual = [' ' if valor == '' else valor for valor in linha]
        print(mapaVisual)
        
def mostrarCordMapa(mapa):
    limpar_terminal()
    print('    1    2    3    4    5  ')

    num = 0
    for linha in mapa:
        num += 1
        mapaVisual = [' ' if valor == '' else valor for valor in linha]
        print(f'{num} {mapaVisual}')
        
        
# MAPA
mapa = [
    ['','','','',''],
    ['','','','',''],
    ['','','','',''],
    ['','','','',''],
    ['','','','',''],
]

mostrarCordMapa(mapa)


# INSERIR OBSTACULOS
qntObstaculos = int(input('\nQuantos obstáculos deseja adicionar?: '))

while qntObstaculos >= 25:
    qntObstaculos = int(input('\nInsira um valor menor que 25!: '))

for i in range(qntObstaculos):
    mostrarCordMapa(mapa)
    
    obstaculo_X = int(input('\nCoordenada X: ')) - 1
    obstaculo_Y = int(input('Coordenada Y: ')) - 1
    
    while obstaculo_X > 4 or obstaculo_Y > 4 or mapa[obstaculo_Y][obstaculo_X] == 'x':
        mostrarCordMapa(mapa)
        print('\nEssas coordenadas ja possuem um obstaculo ou está fora da área!')
        obstaculo_X = int(input('Coordenada X: ')) - 1
        obstaculo_Y = int(input('Coordenada Y: ')) - 1
        
    mapa[obstaculo_Y][obstaculo_X] = 'x'
    
    
# INSERIR JOGADOR
mostrarCordMapa(mapa)

print('Insira o jogador:')
insJogador_X = int(input('\nCoordenada X: ')) - 1
insJogador_Y = int(input('Coordenada Y: ')) - 1

while insJogador_X > 5 or insJogador_Y > 5 or mapa[insJogador_Y][insJogador_X] == 'x':
    mostrarCordMapa(mapa)
    print('Essas coordenadas ja possuem um obstaculo ou está fora da área!')
    insJogador_X = int(input('\nCoordenada X: ')) - 1
    insJogador_Y = int(input('Coordenada Y: ')) - 1

mapa[insJogador_Y][insJogador_X] = 'j'


# MOVIMENTAÇÃO
jogador = 'j'
andar = ''

def cima():

    for linha in mapa:
        if jogador in linha:
            jogador_y = mapa.index(linha)
            jogador_x = linha.index(jogador)

    if mapa[jogador_y - 1][jogador_x] == '':
        mapa[jogador_y][jogador_x] = ''
        jogador_y -= 1
        mapa[jogador_y][jogador_x] = 'j'
        mostrarMapa(mapa)
        print('\nQual direção deseja andar?(w/a/s/d)')
        print('Sair: esc')

def baixo():

    for linha in mapa:
        if jogador in linha:
            jogador_y = mapa.index(linha)
            jogador_x = linha.index(jogador)

    try:
        if mapa[jogador_y + 1][jogador_x] == '':
            mapa[jogador_y][jogador_x] = ''
            jogador_y += 1
            mapa[jogador_y][jogador_x] = 'j'
            mostrarMapa(mapa)
            print('\nQual direção deseja andar?(w/a/s/d)')
            print('Sair: esc')
            
    except IndexError:
        if mapa[0][jogador_x] == '':
            mapa[jogador_y][jogador_x] = ''
            jogador_y = 0
            mapa[jogador_y][jogador_x] = 'j'
            mostrarMapa(mapa)
            print('\nQual direção deseja andar?(w/a/s/d)')
            print('Sair: esc')

def esquerda():

    for linha in mapa:
        if jogador in linha:
            jogador_y = mapa.index(linha)
            jogador_x = linha.index(jogador)

    if mapa[jogador_y][jogador_x - 1] == '':
        mapa[jogador_y][jogador_x] = ''
        jogador_x -= 1
        mapa[jogador_y][jogador_x] = 'j'
        mostrarMapa(mapa)
        print('\nQual direção deseja andar?(w/a/s/d)')
        print('Sair: esc')

def direita():

    for linha in mapa:
        if jogador in linha:
            jogador_y = mapa.index(linha)
            jogador_x = linha.index(jogador)
    try:
        if mapa[jogador_y][jogador_x + 1] == '':
            mapa[jogador_y][jogador_x] = ''
            jogador_x += 1
            mapa[jogador_y][jogador_x] = 'j'
            mostrarMapa(mapa)
            print('\nQual direção deseja andar?(w/a/s/d)')
            print('Sair: esc')
            
    except IndexError:
        if mapa[jogador_y][0] == '':
            mapa[jogador_y][jogador_x] = ''
            jogador_x = 0
            mapa[jogador_y][jogador_x] = 'j'
            mostrarMapa(mapa)
            print('\nQual direção deseja andar?(w/a/s/d)')
            print('Sair: esc')

evento = keyboard.read_event()

mostrarMapa(mapa)
print('\nQual direção deseja andar?(w/a/s/d)')
print('Sair: esc')

while True:
    time.sleep(0.15)

    if keyboard.is_pressed('w'):
        cima()
    elif keyboard.is_pressed('a'):
        esquerda()
    elif keyboard.is_pressed('s'):
        baixo()
    elif keyboard.is_pressed('d'):
        direita()
    elif keyboard.is_pressed('esc'):
        limpar_terminal()
        print(f'Saindo...')
        time.sleep(1)
        limpar_terminal()
        break
    else:
        pass