import random
from colorama import init, Fore, Style

init()

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock, paper, or scissors): ").lower()
            if move in moves:
                return move
            else:
                print("Invalid move! Please enter rock, paper, or scissors.")


class ReflectPlayer(Player):
    def __init__(self):
        self.last_opponent_move = None

    def learn(self, my_move, their_move):
        self.last_opponent_move = their_move

    def move(self):
        if self.last_opponent_move:
            return self.last_opponent_move
        return random.choice(moves)


class CyclePlayer(Player):
    def __init__(self):
        self.last_move_index = -1

    def learn(self, my_move, their_move):
        pass

    def move(self):
        self.last_move_index = (self.last_move_index + 1) % len(moves)
        return moves[self.last_move_index]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print(f"{Fore.GREEN}Player 1 WINS!{Style.RESET_ALL}")
            self.p1_score += 1
        elif beats(move2, move1):
            print(f"{Fore.GREEN}Player 2 WINS!{Style.RESET_ALL}")
            self.p2_score += 1
        else:
            print(f"{Fore.YELLOW}It's a tie!{Style.RESET_ALL}")
        print(f"Score: Player 1 - {self.p1_score}, Player 2 - {self.p2_score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        while True:
            self.play_round()
            if self.p1_score == 3:
                print(f"{Fore.GREEN}Player 1 WINS THE GAME!{Style.RESET_ALL}")
                break
            elif self.p2_score == 3:
                print(f"{Fore.GREEN}Player 2 WINS THE GAME!{Style.RESET_ALL}")
                break
        print(f"Final Score: Player 1 - {self.p1_score}, Player 2 - {self.p2_score}")
        if self.p1_score > self.p2_score:
            print(f"{Fore.GREEN}Player 1 is the overall winner!{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Player 2 is the overall winner!{Style.RESET_ALL}")


if __name__ == '__main__':
    strategies = [RockPlayer(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    for strategy in strategies:
        game = Game(strategy, HumanPlayer())
        game.play_game()
        print("\n" + "=" * 20 + "\n")
