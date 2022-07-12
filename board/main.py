from config import settings
from game.factory import create_board
from game.game_statistics import show_statistics


def main():
    """
    the proposed program must execute 300 simulations,
    printing the data referring to the executions in the console.
    """
    results = []
    i = 1

    while i <= int(settings['ENV_NUMBER_SIMULATION']):
        board = create_board()
        while board.winner is None:
            for player in board.players:
                if player.gameover:
                    board.remove_player(player)
                winner = board.check_winner(player)
                if winner:
                    board.winner = winner
                    break
                board.play(player)
            board.played += 1
        results.append(board.finish())
        i += 1
    show_statistics(results)


if __name__ == "__main__":
    main()
