import fire
from my_helpers import (
    create_user,
    create_joke,
    find_user_by_id,
    find_user_by_name,
    find_joke_by_id,
    find_joke_by_joke,
    list_users,
    list_jokes,
    update_user,
    update_joke,
    delete_user,
    delete_joke,
    exit
)
def main():
    while True:
        print("1. Create user")
        print("2. Create joke")
        print("3. Find user by id")
        print("4. Find user by name")
        print("5. Find joke by id")
        print("6. Find joke by joke")
        print("7. List users")
        print("8. List jokes")
        print("9. Update user")
        print("10. Update joke")
        print("11. Delete user")
        print("12. Delete joke")
        print("13. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_user()
        elif choice == "2":
            create_joke()
        elif choice == "3":
            find_user_by_id()
        elif choice == "4":
            find_user_by_name()
        elif choice == "5":
            find_joke_by_id()
        elif choice == "6":
            find_joke_by_joke()
        elif choice == "7":
            list_users()
        elif choice == "8":
            list_jokes()
        elif choice == "9":
            update_user()
        elif choice == "10":
            update_joke()
        elif choice == "11":
            delete_user()
        elif choice == "12":
            delete_joke()
        elif choice == "13":
            exit()
        else:
            print("Invalid choice")

    if__name__ == "__main__"
fire.Fire(main)
    