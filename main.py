from time import sleep
from game_manager import GameManager

if __name__ == '__main__':
    game = GameManager()
    try:
        while True:
            game.draw()
            game.update()
            sleep(0.3)
    except KeyboardInterrupt:
        print('\nGood Bye!')
