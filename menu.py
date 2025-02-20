class Event:
    def monday(self):
        print("Today is Cultural fest.")

    def tuesday(self):
        print("Today is Sports day.")

    def wednesday(self):
        print("Today is Ethnic day.")

    def other_day(self):
        print('Invalid choice enetered')
        
class Menu:
    def __init__(self):
        pass
    def get_menu(self, events):
        menu = {
                1 : events.monday,
                2 : events.tuesday,
                3 : events.wednesday
            }
        return menu
    def run_menu(self):
        event = Event()
        while True:
            choice = int(input('1:Monday 2:Tuesday 3:wednesday. (-1 to exit) Your choice: '))
            if choice == -1:
                break
            menu = self.get_menu(event)
            menu.get(choice, event.other_day)()
        print('End of program')


menu = Menu()        
menu.run_menu()