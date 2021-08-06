import time
#ниже мне нужно подольше задержать текст на экране
def display_board():
    blankboard = """
    _________
    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |
    """
#создаем вид поля по умолчанию
    for i in range(1, 10):
        if board[i] == "X" or board[i] == "O":
        #берем значения из списка, где хранятся ходы игроков
        #если там что-то есть, отображаем это на доске
            blankboard = blankboard.replace(str(i), board[i])
    print(blankboard)
    #печатаем обновленную доску

def pick_your_side():
    #Эта функция выбирает, кто кем будет играть
    first_player = None
    second_player = None
    #Приходится обнулять значения. Есть ли более изящное решение?
    first_player = input("Pick your side, X or O? ").upper()
    #Игрок должен ввести, за кого он играет.
    #Сразу переводим в заглавные буквы, чтобы было меньше проверок
#при приеме результата
    while first_player != "X" and first_player != "O":
#Заставляет игрока ввести правильный вариант.
# Не принимает ничего, кроме Х и О.
        first_player = input("Unexpected input. Please, select X or O ").upper()
    if first_player == "X":
        second_player = "O"
    else:
        second_player = "X"
    #Присваивает второму игроку противоположный знак.
    print(f"First player is {first_player}")
    print(f"Second player is {second_player}")
    time.sleep(1.2)
    #Мне удобно, чтобы сообщение о том, кто сколько играет какое-то время
    #было на экране
    return first_player, second_player
#значения нам пригодятся ниже
def expected_input(player_input):
    #Проверяет, что игорк ввел допустимое значение
    if player_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Wrong input. Please, enter a number from 1 to 9 ")
        return False
    #Первая проверка заставляет ввести цифры с 1 до 9, и ничто иное
    if board[int(player_input)] != "#":
        print("This place is occupied. Choose another. ")
        #Эта часть проверяет, не занята ли клетка.
        # По дефолту еще не занятые клетки в списке, которое хранит
        # состояние поле, обозначается "#".
        return False
    return True
#Функция возвращает "Ложь" до тех пор, пока игрок не выберет
# допустимое значение
def endgame_full_board(board):
    return board.count("#") > 1
#Проверяем, остались ли еще свободные клетки на поле.
# Один "#" остается, потому что для интуитивности мы начинали отсчет
# в списке, который хранит поле, не с 0, а с 1.
def endgame_win(player, board):
#Здесь перечислены условия победы
#Эта функция принимает в качестве аргумента игрока(то есть "Х" или "О")
# и состояние доски

    if player == board[1] == board[2] == board[3]:
        print("**********")
        return True
    elif player == board[4] == board[5] == board[6]:
        print("**********")
        return True
    elif player == board[7] == board[8] == board[9]:
        print("**********")
        return True
    elif player == board[1] == board[4] == board[7]:
        print("**********")
        return True
    elif player == board[2] == board[5] == board[8]:
        print("**********")
        return True
    elif player == board[3] == board[6] == board[9]:
        print("**********")
        return True
    elif player == board[1] == board[5] == board[9]:
        print("**********")
        return True
    elif player == board[3] == board[5] == board[7]:
        print("**********")
        return True
    else:
        return False

def select_square(player):
#Берет у игрока информацию о том, куда он хочет поставить свою фишку
    player_input = input(f"For {player} select square from 1 to 9 ")
    while not expected_input(player_input):
#Проверяет, можно ли туда поставить фишку и корректно ли введено значение
#Работает, пока expected input не вернет True.
        player_input = input(f" For {player} select square from 1 to 9 ")
    return player_input
#Получив корректное значение, возвращает его в основную программу

def update_the_board(board, selected_place, player):
#Функция берет состояние доски + место, куда игрок хочет поставить свою
# фишку + маркер игрока (Х и О)
    board[int(selected_place)] = player
#По индексу selected_place в списке board, который хранит состояние поля,
#прописываем фишку игорка
    display_board()
#рисует обновленное поле

def gameloop():
#Основной цикл игры
    global victories_of_the_first_player
    global victories_of_the_second_player
    global ties
#Хотим вести счет побед и поражений, поэтому сделали глобальные
# переменные вне функции, чтобы они не обнулялись, когда партия
# закончится
    first_player, second_player = pick_your_side()
#Даем игрокам выбрать, за кого играть, Х или О
    display_board()
#Рисуем пустую доску
    while endgame_full_board(board):
#Пока у нас не заполнилась доска (пока оно True), выполняем алгорим
        position = select_square(first_player)
#Даем игроку выбрать, куда поставить фишку, вызывая функцию, которая
#вызывает другую функцию...
#Записываем результат в переменную, потому что по-другому не работает
        update_the_board(board, position, first_player)
#Обновляем список, где хранится состояние игры (не строку, которая
# выводится в консоль, чтобы показать состояние поля)
        if endgame_win(first_player, board):
#Если наступило условие победы, мы поздравляем игрока, записываем ему
# плюс одно очко, прерываем цикл
            print(f"Congratulations, {name_of_the_first_player}! The victory is yours.")
            victories_of_the_first_player += 1
            break
        if not endgame_full_board(board):
#Из названия переменной это не очевидно, но имеется в виду, что поле
#заполнено. То есть когда оно заполнится, а условие победы так и не
#наступило, высветится "ничья". То есть когда поле заполнится,
# получится not False, и условие выполнится.
            print("Tie")
            ties += 1
            break
        position = select_square(second_player)
#Повторяем то же самое для второго игрока, потому что не хватило времени,
#чтобы вставить и протестировать нормальное чередование ходов
#нужно было сделать счетчик, по четным ходит один, по нечетным второй
        update_the_board(board, position, second_player)
        if endgame_win(second_player, board):
            print(f"Congratulations, {name_of_the_second_player}! The victory is yours.")
            victories_of_the_second_player += 1
            break
    print("Game over")

name_of_the_first_player = input("Greetings, first player! What is your name? ")
name_of_the_second_player = input("Greetings, first player! What is your name? ")
victories_of_the_first_player = 0
victories_of_the_second_player = 0
ties = 0
#В этих переменных мы храним имена игорок и счет партий
while True:
#Это бесконечный цикл. Пока игрок согласен играть, будем запускать game_loop.
    reply = input("""Do you wish play? 
    'Yes' or 'No'? """).upper()
    if reply not in ["YES", "NO"]:
        print("Wrong input")
    else:
        if reply == "YES":
            board = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
            gameloop()
        else:
            print(f"""
{name_of_the_first_player} won {victories_of_the_first_player} times
{name_of_the_second_player} won {victories_of_the_second_player} times
{ties} ties
Goodbye!""")
            break
            #Если игрок отказался играть дальше, мы ему рассказываем,
            # кто выиграл и прерываем цикл
