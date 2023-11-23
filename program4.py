import math
from pyfiglet import Figlet
import colorama

colorama.init()

def for_print(text, color):
    print(color + text + colorama.Style.RESET_ALL)

def colored_letter(text, color):
    return color + text + colorama.Style.RESET_ALL

def buying_apple(total_money, apple_price):
    maximum_apple = total_money // apple_price
    return maximum_apple

def main():
    font = Figlet(font='small')
    font_one = Figlet(font='digital')
    font_two = Figlet(font='script')
    font_three = Figlet(font='big')

    for_print(colored_letter(font.renderText("Greetings! Welcome to Apple Shop!"), colorama.Fore.MAGENTA), colorama.Fore.MAGENTA)

    try:
        total_money = float(input("Please enter your total money: "))
        apple_price = float(input("Please enter the price of apple you wish to buy: "))
    except ValueError:
        for_print("Invalid input. Please enter numeric values.", colorama.Fore.RED)
        return    
    

    apple_max = buying_apple(total_money, apple_price)


    for_print(colored_letter(font.renderText("Since your money is:"), colorama.Fore.BLUE), colorama.Fore.BLUE)
    for_print(colored_letter(font_one.renderText(f"{total_money}$"), colorama.Fore.GREEN), colorama.Fore.GREEN)
    for_print(colored_letter(font.renderText("The number of apples that you can buy is:"), colorama.Fore.BLUE), colorama.Fore.BLUE)
    for_print(colored_letter(font_two.renderText(f"{math.floor(apple_max)}"), colorama.Fore.YELLOW), colorama.Fore.YELLOW)
    for_print(colored_letter(font.renderText("The total money left to you after buying is:"), colorama.Fore.BLUE), colorama.Fore.BLUE)
    for_print(colored_letter(font_three.renderText(f"{total_money % apple_price}$"), colorama.Fore.RED), colorama.Fore.RED)

if __name__ == "__main__":
    main()
