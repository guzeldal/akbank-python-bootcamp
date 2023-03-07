import csv
import datetime


class Pizza:
    def __init__(self):
        self.description = "Bir Pizza"
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return 0


class PizzaDecorator(Pizza):
    def __init__(self, component):
        self.component = component
    
    def get_description(self):
        return self.component.get_description() + ", " + Pizza.get_description(self)
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)


class KlasikPizza(Pizza):
    def __init__(self):
        self.description = "Klasik Pizza"
    
    def get_cost(self):
        return 15


class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
    
    def get_cost(self):
        return 20


class TurkishPizza(Pizza):
    def __init__(self):
        self.description = "Türk Pizza"
    
    def get_cost(self):
        return 18


class DominosPizza(Pizza):
    def __init__(self):
        self.description = "Sade Pizza"
    
    def get_cost(self):
        return 12


class OliveSauce(PizzaDecorator):
    def __init__(self, component):
        self.component = component
        self.description = "Zeytin Soslu"


class MushroomSauce(PizzaDecorator):
    def __init__(self, component):
        self.component = component
        self.description = "Mantarlı"


class GoatCheeseSauce(PizzaDecorator):
    def __init__(self, component):
        self.component = component
        self.description = "Keçi Peynirli"


class MeatSauce(PizzaDecorator):
    def __init__(self, component):
        self.component = component
        self.description = "Et Soslu"


class OnionSauce(PizzaDecorator):
    def __init__(self, component):
        self.component = component
        self.description = "Soğan Soslu"


class CornSauce(PizzaDecorator):
    def __init__(self, component):
        self.component = component
        self.description = "Mısır Soslu"



# Main function
def main():
    # Print menu
    with open("./menu.txt", 'r', encoding="utf-8") as menu_file:
        menu_text = menu_file.read()
        print(menu_text)

    # Prompt user to select pizza and sauce
    pizza = None
    sauce = None
    while pizza is None:
        pizza_input = input("Please select a pizza: ")
        if pizza_input == "1":
            pizza = KlasikPizza()
        elif pizza_input == "2":
            pizza = MargheritaPizza()
        elif pizza_input == "3":
            pizza = TurkishPizza()
        elif pizza_input == "4":
            pizza = DominosPizza()
        else:
            print("Invalid input. Please try again.")

    while sauce is None:
        sauce_input = input("Please select a sauce: ")
        if sauce_input == "11":
            sauce = OliveSauce(pizza)
        elif sauce_input == "12":
            sauce = MushroomSauce(pizza)
        elif sauce_input == "13":
            sauce = GoatCheeseSauce(pizza)
        elif sauce_input == "14":
            sauce = MeatSauce(pizza)
        elif sauce_input == "15":
            sauce = OnionSauce(pizza)
        elif sauce_input == "16":
            sauce = CornSauce(pizza)
        else:
            print("Invalid input. Please try again.")

    # Calculate total cost
    total_cost = sauce.get_cost()

    # Prompt user for personal information
    name = input("Please enter your name: ")
    tc_no = input("Please enter your TC identity number: ")
    cc_no = input("Please enter your credit card number: ")
    cc_cvv = input("Please enter your credit card CVV: ")

    # Write order to database
    with open('Orders_Database.csv', 'a') as orders_file:
        writer = csv.writer(orders_file)
        now = datetime.datetime.now()
        writer.writerow([name, tc_no, cc_no, sauce.get_description(), now.strftime("%Y-%m-%d %H:%M:%S"), cc_cvv])

    # Print order summary
    print("\nOrder Summary:")
    print("Pizza: {}".format(pizza.get_description()))
    print("Sauce: {}".format(sauce.get_description()))
    print("Total Cost: {} TL".format(total_cost))
    print("Thank you for your order, {}!".format(name))

if __name__ == "__main__":
    main()
