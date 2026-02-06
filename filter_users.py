import json


def load_users(filename="users.json"):
    """Load users from a JSON file and return them as a list."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def filter_users_by_name(users, name):
    """Return users whose name matches (case-insensitive)."""
    name = name.strip().lower()
    return [user for user in users if user.get("name", "").lower() == name]


def filter_users_by_age(users, age):
    """Return users whose age matches exactly."""
    return [user for user in users if user.get("age") == age]


def print_users(users):
    """Print users in a readable way."""
    if not users:
        print("No users found.")
        return

    for user in users:
        print(user)


def main():
    users = load_users()

    filter_option = input(
        "What would you like to filter by? (name/age): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filtered = filter_users_by_name(users, name_to_search)
        print_users(filtered)

    elif filter_option == "age":
        age_raw = input("Enter an age to filter users: ").strip()

        if not age_raw.isdigit():
            print("Invalid age. Please enter a whole number (e.g. 25).")
            return

        age_to_search = int(age_raw)
        filtered = filter_users_by_age(users, age_to_search)
        print_users(filtered)

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
