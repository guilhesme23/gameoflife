import os
from time import sleep
import numpy as np

WIDTH = 400
HEIGHT = 180
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

class GameManager():
    def __init__(self, width=400, height=180, res=10):
        self.width = width
        self.height = height
        self.res = res
        self.size = (int(self.height / self.res), int(self.width / self.res))

        self.cells, self.neighbours = self._build_initial_state()

    def _build_initial_state(self):
        rows, cols = self.size
        cells = np.random.randint(0,2,size=(rows, cols))
        neighbours = self._get_neighbours(cells)
        return cells, neighbours


    def draw(self):
        os.system('clear')
        print('')
        print('')
        for cells in self.cells:
            for cell in cells:
                if cell:
                    # █
                    print(f'{bcolors.FAIL}█{bcolors.ENDC}', end=' ')
                else:
                    print(f'{bcolors.OKBLUE}_{bcolors.ENDC}', end=' ')
            print('')
            print('')

    def _get_neighbours(self, cells):
        rows, cols = self.size
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

    def update(self):
        rows, cols = self.size
        new_generation = np.zeros(self.cells.shape, dtype=np.int)
        for row in range(rows):
            for col in range(cols):
                loc = (row, col)
                # Rule 1: Qualquer celula viva com menos de 2 vizinhos morre de solidão
                if self.cells[loc] and self.neighbours[loc] < 2:
                    new_generation[loc] = 0
                # Rule 2: Qualquer celula viva com mais de 3 vizinhos morre de superpopulação
                elif self.cells[loc] and self.neighbours[loc] > 3:
                    new_generation[loc] = 0
                # Rule 3: Qualquer celula morta com exatamente 3 vizinhos se torna viva
                elif not self.cells[loc] and self.neighbours[loc] == 3:
                    new_generation[loc] = 1
                # Rule 4: Qualquer celula viva com 2 ou 3 vizinhos permanece para a próxima geração
                elif self.cells[loc] and (self.neighbours[loc] == 2 or self.neighbours[loc] == 3):
                    new_generation[loc] = self.cells[loc]
        new_neighbours = self._get_neighbours(new_generation)
        self.cells = new_generation
        self.neighbours = new_neighbours

    def read_state_from_file(filename):
        with open(filename, 'rb') as f:
            self.rows, self.cols, self.res = f.readline().decode('utf-8').strip('\n').split(' ')[1:]
            self.cells = np.loadtxt(f, dtype=np.int)

    def write_state_to_file(filename):
        with open(filename, 'w') as f:
            np.savetxt(f,cells, header=f'{self.size[0]} {self.size[1]} {self.res}', fmt='%d')
