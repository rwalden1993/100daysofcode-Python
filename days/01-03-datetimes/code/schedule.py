from datetime import date


#global variables
schedule = {}
quit_program = False

def handle_user_input(user_input):
    global quit_program
    if user_input == 'add':
        add_event()
    elif user_input == 'view':
        print_schedule()
    elif user_input == 'delete':
        delete_entry()
    elif user_input == 'quit':
        quit_program = True


def add_event():
    global schedule
    date_string = input("Enter date (yyyy-mm-dd):")
    event = input("Enter event: ")
    schedule[event] = date.fromisoformat(date_string)
    print(f'{event} added to schedule')

def print_schedule():
    global schedule
    for x, y in schedule.items():
        print(x, y)

def delete_entry():
    global schedule
    event = input('Event to delete: ')
    schedule.pop(event)

if __name__ == '__main__':
    # begin program
    print("Hello! Welcome to your schedule!")
    print("Options:")
    print("\t \'add\'    : Add new event to your schedule")
    print("\t \'view\'   : View your schedule")
    print("\t \'delete\' : Delete an event from your schedule")
    print("\t \'quit\'   : Quit the program")
    print('')

    while not quit_program:
        user_input = input('Command: ')
        handle_user_input(user_input)
