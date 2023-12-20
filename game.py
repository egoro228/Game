import random

def user_turn(stones):
    while True:
        try:
            user_input = int(input("Ваш ход. Введите количество камней (1-3): "))
            if 1 <= user_input <= 3 and user_input <= stones:
                return user_input
            else:
                print("Некорректный ввод. Пожалуйста, введите число от 1 до 3 и не больше оставшихся камней.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

def computer_turn(stones):
    return random.randint(1, min(3, stones))

def play_game():
    stones = random.randint(4, 30)
    print(f"Начальное количество камней: {stones}")

    while stones > 0:
        user_choice = user_turn(stones)
        stones -= user_choice
        print(f"Осталось камней: {stones}")

        if stones == 0:
            print("Вы выиграли!")
            break

        computer_choice = computer_turn(stones)
        stones -= computer_choice
        print(f"Компьютер взял {computer_choice} камней. Осталось камней: {stones}")

        if stones == 0:
            print("Компьютер выиграл!")

if __name__ == "__main__":
    play_game()
