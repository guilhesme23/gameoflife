import argparse
from time import sleep
from game_manager import GameManager

def build_args():
    parser = argparse.ArgumentParser('Run Conway\'s Game of Life')
    parser.add_argument('--from-file', type=str)
    parser.add_argument('--save-init-state', type=str)
    parser.add_argument('--save-final-state', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = build_args()
    if args.from_file:
        game = GameManager(from_file=args.from_file)
    elif args.save_init_state:
        game = GameManager(save_initial_state=args.save_init_state)
    else:
        game = GameManager()

    try:
        while True:
            game.draw()
            game.update()
            sleep(0.3)
    except KeyboardInterrupt:
        print('\nGood Bye!')
