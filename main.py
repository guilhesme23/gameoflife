import os
from time import sleep
import numpy as np

WIDTH = 300
HEIGHT = 150
RES = 10

SIZE = (int(HEIGHT / RES), int(WIDTH / RES))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def draw_generation(array):
    os.system('clear')
    print('')
    print('')
    for cells in array:
        for cell in cells:
            if cell:
                print(f'{bcolors.FAIL}█{bcolors.ENDC}', end=' ')
            else:
                print(f'{bcolors.OKBLUE}█{bcolors.ENDC}', end=' ')
        print('')
        print('')

def get_neighbours(cells, rows, cols):
    neighbours = {}
    for row in range(rows):
        for col in range(cols):
            neighbours[(row,col)] = np.sum(
                cells[
                    max(row-1, 0):row+2,
                    max(col-1,0):col+2
                ]
            )
            if cells[row,col]:
                neighbours[(row, col)] -= 1
    return neighbours

def build_initial_state(rows, cols):
    cells = np.random.randint(0,2,size=(rows, cols))
    neighbours = get_neighbours(cells, rows, cols)
    return cells, neighbours

def calc_new_generation(cells, neighbours):
    rows, cols = cells.shape
    new_generation = np.zeros(cells.shape, dtype=np.int)
    for row in range(rows):
        for col in range(cols):
            loc = (row, col)
            # Rule 1: Qualquer celula viva com menos de 2 vizinhos morre de solidão
            if cells[loc] and neighbours[loc] < 2:
                new_generation[loc] = 0
            # Rule 2: Qualquer celula viva com mais de 3 vizinhos morre de superpopulação
            elif cells[loc] and neighbours[loc] > 3:
                new_generation[loc] = 0
            # Rule 3: Qualquer celula morta com exatamente 3 vizinhos se torna viva
            elif not cells[loc] and neighbours[loc] == 3:
                new_generation[loc] = 1
            # Rule 4: Qualquer celula viva com 2 ou 3 vizinhos permanece para a próxima geração
            elif cells[loc] and (neighbours[loc] == 2 or neighbours[loc] == 3):
                new_generation[loc] = cells[loc]
    new_neighbours = get_neighbours(new_generation, *new_generation.shape)
    return new_generation, new_neighbours

if __name__ == '__main__':
    cells, n = build_initial_state(*SIZE)
    try:
        while True:
            draw_generation(cells)
            cells, n = calc_new_generation(cells, n)
            sleep(0.3)
    except KeyboardInterrupt:
        pass