from pyfiglet import Figlet
import colorama

colorama.init()

def for_print(letter, color):
    print(color + letter + colorama.Style.RESET_ALL)

def colored_letter(letter, color):
    return color + letter + colorama.Style.RESET_ALL

def fruit_shop(applenum, apple_price, orangenum, orange_price):
    return (applenum * apple_price) + (orangenum * orange_price)

def main():
    font = Figlet(font='small')
    font_one = Figlet(font='bubble')
    font_two = Figlet(font='slant')
    font_three = Figlet(font='big')

    apple_price = 20
    orange_price = 25
    
    for_print(colored_letter(font.renderText("Welcome to Fruit Ninja Shop!"), colorama.Fore.RED), colorama.Fore.RED)
    
    applenum = int(input("How many apples do you want to buy?: "))
    orangenum = int(input("How many oranges do you want to buy?: "))

    for_print(colored_letter(font_two.renderText(f"The total cost of buying {applenum} apples is equals to: " + str(apple_price * applenum)), colorama.Fore.GREEN), colorama.Fore.GREEN)
    for_print(colored_letter(font_one.renderText(f"The total cost of buying {orangenum} oranges is equals to: " + str(orange_price * orangenum)), colorama.Fore.BLUE), colorama.Fore.BLUE)

    total_cost = fruit_shop(applenum, apple_price, orangenum, orange_price) 
    for_print(colored_letter(font_three.renderText(f"Your overall total cost is: {total_cost}"), colorama.Fore.YELLOW), colorama.Fore.YELLOW)

if __name__ == "__main__":
    main()
