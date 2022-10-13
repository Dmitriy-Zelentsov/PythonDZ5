# Создайте программу для игры в ""Крестики-нолики"".
pole = list(range(1, 10))


def draw_pole(pole):
    for i in range(3):
        print("_", pole[0+i*3], "_", pole[1+i*3], "_", pole[2+i*3], "_")


def take_input(player):
    valid = False
    while not valid:
        playeranswer = input("Куда поставим " + player+"? ")
        try:
            playeranswer = int(playeranswer)
        except:
            print("Вы ввели число вне диапазона")
            continue
        if playeranswer >= 1 and playeranswer <= 9:
            if (str(pole[playeranswer-1]) not in "XO"):
                pole[playeranswer-1] = player
                valid = True
            else:
                print("Эта место занято")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить")

def check_win(pole):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if pole[each[0]] == pole[each[1]] == pole[each[2]]:
            return pole[each[0]]
    return False


def main(pole):
    counter = 0
    win = False
    while not win:
        draw_pole(pole)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(pole)
            if tmp:
                print(tmp, "победил!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_pole(pole)

main(pole)
