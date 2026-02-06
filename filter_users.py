import json


def load_users(path="users.json"):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def filter_users_by_name(name):
    users = load_users()
    name_lower = name.strip().lower()
    return [u for u in users if u["name"].strip().lower() == name_lower]


def filter_users_by_age(age):
    users = load_users()
    return [u for u in users if u["age"] == age]


def filter_users_by_email(email):
    users = load_users()
    email_lower = email.strip().lower()
    return [u for u in users if u["email"].strip().lower() == email_lower]


def print_users(users):
    if not users:
        print("No matching users found.")
        return
    for user in users:
        print(user)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (name/age/email): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        print_users(filter_users_by_name(name_to_search))

    elif filter_option == "age":
        age_str = input("Enter an age to filter users: ").strip()
        if not age_str.isdigit():
            print("Age must be a number.")
        else:
            print_users(filter_users_by_age(int(age_str)))

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        print_users(filter_users_by_email(email_to_search))

    else:
        print("Filtering by that option is not yet supported.")
