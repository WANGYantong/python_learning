import random


def roll_dice(numbers=3, points=None):
    print("<<<<< ROLL THE DICE! >>>>>")
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points


def roll_result(total):
    is_big = 11 <= total <= 18
    is_small = 3 <= total <= 10
    if is_big:
        return "Big"
    elif is_small:
        return 'Small'


def amount_count(win, total, bet, rate=1):
    if win:
        total = total + bet * rate
    else:
        total = total - bet * rate
    return total


def start_game():
    amount = 1000
    while amount > 0:
        print("<<<<< GAME STARTS! >>>>>")
        choices = ["Big", "Small"]
        your_choices = input("Big or Small:")
        bet_input = int(input("How much you wanna bet ? - "))
        rate_input = int(input("How many rates you wanna ? - "))
        bet_money = bet_input * int(rate_input)
        if bet_money <= amount:
            if your_choices in choices:
                points = roll_dice()
                total = sum(points)
                you_win = your_choices == roll_result(total)
                amount = amount_count(you_win, amount, bet_input, rate_input)
                if you_win:
                    print("The points are {} You Win!".format(points))
                    print("You gained {}, you have {} now".format(bet_money, amount))
                else:
                    print("The points are {} You Lose!".format(points))
                    print("You lost {}, you have {} now".format(bet_money, amount))
            else:
                print("Invalid Words!")
        else:
            print("Your don't have so much amount!")
    else:
        print("GAME OVER!")

start_game()