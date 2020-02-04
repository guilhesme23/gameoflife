import argparse
from time import sleep
from game_manager import GameManager

def build_args():
    parser = argparse.ArgumentParser('Run Conway\'s Game of Life')
    parser.add_argument('--load-txt', type=str)
    parser.add_argument('--load-bin', type=str)
    parser.add_argument('--save-init-txt', type=str)
    parser.add_argument('--save-init-bin', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = build_args()
    if args.load_txt:
        game = GameManager(from_file=args.load_txt)
    elif args.load_bin:
        game = GameManager.load_bin(args.load_bin)
    else:
        game = GameManager()

    if args.save_init_txt:
        game.save_txt(args.save_init_txt)

    if args.save_init_bin:
        game.save_bin(args.save_init_bin)

    try:
        while True:
            game.draw()
            game.update()
            sleep(0.3)
    except KeyboardInterrupt:
        print('\nGood Bye!')
