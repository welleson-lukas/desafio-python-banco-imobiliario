from collections import Counter


def show_statistics(results):
    total_timeout = sum([1 for result in results if result["time_out"]])
    total_played = sum([result["played"] for result in results])
    count_winner = Counter()
    for result in results:
        strategy = str(result['strategy'])
        count_winner[strategy] += 1

    print(
        f'''Quantas partidas terminam por timeout: '''
        f'''{total_timeout}'''
    )

    print(
        f'''Quantos turnos em média demora uma partida: '''
        f'''{total_played / len(results):.1f}'''
    )

    print("Qual a porcentagem de vitórias por comportamento dos jogadores:")
    for strategy, winner in count_winner.most_common():
        print("  *  ", f"{strategy}: {(winner * 100) // len(results)}%")

    print(
        f'''Qual o comportamento que mais venceu:
        {count_winner.most_common(1)[0][0]}
        venceu: {count_winner.most_common(1)[0][1]} vezes'''
    )
