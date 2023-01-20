board = list(range(1,10))
wins_records = [(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7),(1,4,7),(2,5,8),(3,6,9)]
def gameboard():
    print('-------------')
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|") #Заполнение
        print('------------')
def take_input(player_token):
    while True:
        value = input('Поставьте знак: ' + player_token)
        if not (value in '123456789'):
            print('Неверный ввод')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Клетка уже занята')
            continue
        board[value - 1] = player_token
        break

def check_winner():
    for i in wins_records:
        if (board[i[0]-1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[1] - 1]
    else:
        return False
def main():
    counter = 0
    while True:
        gameboard()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = check_winner()
            if winner:
                gameboard()
                print(winner,'Победил')
                break
        counter += 1
        if counter > 8:
            gameboard()
            print('Ничья')
            break
main()