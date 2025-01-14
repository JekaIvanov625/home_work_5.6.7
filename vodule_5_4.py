def main():
    contacts = {"Женя": "666948981"}

    def input_error(func):
        "обробка помилок введення"
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError:
                return "Contact not found."
            except ValueError:
                return "Give me name and phone please."
            except IndexError:
                return "Invalid command. Please check the input."
        return wrapper

    def parse_input(user_input):
        " введення користувача"
        parts = user_input.strip().lower().split(maxsplit=2)
        command = parts[0]
        args = parts[1:] if len(parts) > 1 else []
        return command, args

    @input_error
    def add_contact(args):
        " Додати контакт"
        if len(args) < 2:
            raise ValueError
        name, phone = args
        contacts[name] = phone
        return "Contact added."

    @input_error
    def change_contact(args):
        "Змінити номер телефону "
        if len(args) < 2:
            raise ValueError
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            raise KeyError

    @input_error
    def show_phone(args):
        "Показати номер телефону "
        if len(args) < 1:
            raise ValueError
        name = args[0]
        if name in contacts:
            return f"{name}: {contacts[name]}"
        else:
            raise KeyError

    def show_all():
        " Показати контакти"
        if not contacts:
            return "No contacts found."
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()