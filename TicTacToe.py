# Инициализация карты
table = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Инициализация победных линий
win_lines = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран
def print_maps():
    print(table[0], end=" ")
    print(table[1], end=" ")
    print(table[2])
    print(table[3], end=" ")
    print(table[4], end=" ")
    print(table[5])
    print(table[6], end=" ")
    print(table[7], end=" ")
    print(table[8])

# Узнаем имена игроков
print("Добро пожаловать в игру!!!")
player_1 = input("Введите ваше имя: ")
player_2 = input("Введите ваше имя: ")


#Меняем цифру на символ
def convert(numm, symb):
    numm = table.index(numm)
    table[numm] = symb

#Проверка победы
def victory():
    win = ""
    for i in win_lines:
        if table[i[0]] == "X" and table[i[1]] == "X" and table[i[2]] == "X":
            win = player_1
        if table[i[0]] == "O" and table[i[1]] == "O" and table[i[2]] == "O":
            win = player_2
    return win


game_over = True
X = True
while game_over == True:
    print_maps()
    if X == True:
        symb = "X"
        numm = int(input(f"{player_1}, ваш ход: "))
    else:
        symb = 'O'
        numm = int(input(f"{player_2}, ваш ход: "))

    convert(numm, symb)
    win = victory()
    if win != "":
        game_over = False
    X = not (X)
print_maps()
print(f"Победителем стал: {win}")