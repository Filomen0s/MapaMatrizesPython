import os

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
    limpar_terminal()
    qntObstaculos = int(input('\nInsira um valor menor que 25!: '))

for i in range(qntObstaculos):
    mostrarCordMapa(mapa)
    
    obstaculo_X = int(input('\nCoordenada X: ')) - 1
    obstaculo_Y = int(input('Coordenada Y: ')) - 1
    
    while mapa[obstaculo_Y][obstaculo_X] == 'x':
        mostrarCordMapa(mapa)
        print('Essas coordenadas ja possuem um obstaculo!')
        obstaculo_X = int(input('\nCoordenada X: ')) - 1
        obstaculo_Y = int(input('Coordenada Y: ')) - 1
        
    mapa[obstaculo_Y][obstaculo_X] = 'x'
    
    
# INSERIR JOGADOR
mostrarCordMapa(mapa)

print('Insira o jogador:')
insJogador_X = int(input('\nCoordenada X: ')) - 1
insJogador_Y = int(input('\nCoordenada Y: ')) - 1

while mapa[insJogador_Y][insJogador_X] == 'x':
    mostrarCordMapa(mapa)
    print('Essas coordenadas ja possuem um obstaculo!')
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
            
    except IndexError:
        mapa[jogador_y][jogador_x] = ''
        jogador_y = 0
        mapa[jogador_y][jogador_x] = 'j'

def esquerda():

    for linha in mapa:
        if jogador in linha:
            jogador_y = mapa.index(linha)
            jogador_x = linha.index(jogador)

    if mapa[jogador_y][jogador_x - 1] == '':
        mapa[jogador_y][jogador_x] = ''
        jogador_x -= 1
        mapa[jogador_y][jogador_x] = 'j'

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
    except IndexError:
        mapa[jogador_y][jogador_x] = ''
        jogador_x = 0
        mapa[jogador_y][jogador_x] = 'j'

while True:
    mostrarMapa(mapa)
    
    andar = input('\nQual direção deseja andar?(w/a/s/d): ')
    if True != 'x':
        if andar == 'w':
            cima()
        elif andar == 'a':
            esquerda()
        elif andar == 's':
            baixo()
        elif andar == 'd':
            direita()
        else:
            pass