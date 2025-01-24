def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        # перевіряємо чи контакт існує якщо ТАК тоді нічого не змінюємо
        if name in contacts.keys():
            return "Contact alredy exist."
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Arguments not correct. Example: 'add [name] [phone number]'"
    
def change_contact(args, contacts):
    try:
        name, phone = args
        # перевіряємо чи контакт існує якщо НІ тоді нічого не змінюємо
        if not (name in contacts.keys()):
            return "Contact doesn't exist."
        contacts[name] = phone
        return "Contact updated."
    except ValueError:
        return "Arguments not correct. Example: 'change [name] [phone number]'"
    
def show_phone(args, contacts):
    try:   
        name, = args
        # перевіряємо чи контакт існує в списку і повертаємо одразу значення
        return contacts.get(name) if name in contacts.keys() else "Cannot find contact"
    except ValueError:
        return "Arguments not correct. Example: 'phone [name]'"
    
    
def show_all(args, contacts):
    # тут я вирішив зробити перевірку якщо до команди додано будь-які аргументи то вона не працює коректно
    if not args:
        return contacts
    else:
        return "Command don't recive any arguments. Example: 'all'"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
