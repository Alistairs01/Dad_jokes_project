# Dad_Jokes

## Introduction
A command-line interface (CLI) application for managing users and their jokes. This application allows you to create, update, delete, and list users and jokes, with data persistence in a SQLite database.

###  Features
User Management

1:Create a new user
2:Find a user by ID or username
3:List all users
4:Update user details
5:Delete a user


Joke Management

1:Create a new joke
2:Find a joke by ID or joke text
3:List all jokes
4:Update a joke
5:Delete a joke

####    Prerequisites
.Python version 3.8 must be installed
.VsCode must be installed


#### Installation
After making sure you have both prerequisites , you can begin the following steps

1.Fork and clone the repository 
```sh
git@github.com:Alistairs01/Dad_jokes_project.git
```
2.Navigate to the Directory
```sh
cd Dad_jokes_project/lib
```
3.Run the program 
```sh 
python lib/my_debug.py
 
my_cli.py
```

If you encounter a "permission denied" error, run:
    ```sh
    chmod +x lib/my_cli.py
    ```

Menu Options
👤 Create user - Add a new user to the database.
😂 Create joke - Add a new joke to the database.
🔍 Find user by ID - Search for a user by their ID.
🔍 Find user by name - Search for a user by their username.
🔍 Find joke by ID - Search for a joke by its ID.
🔍 Find joke by joke - Search for a joke by its text.
📋 List users - List all users in the database.
📋 List jokes - List all jokes in the database.
✏️ Update user - Update the details of an existing user.
✏️ Update joke - Update the details of an existing joke.
❌ Delete user - Remove a user from the database.
❌ Delete joke - Remove a joke from the database.
🚪 Exit - Exit the application.


######   Example Commands
Create a User:

Enter 1 at the menu prompt and follow the instructions to input the username and email.
Create a Joke:

Enter 2 at the menu prompt and follow the instructions to input the user ID and the joke text.
List All Users:

Enter 7 at the menu prompt to display all users in the database.
Delete a User:

Enter 11 at the menu prompt and follow the instructions to input the user ID.
Project Structure
.
├── models
│   ├── __init__.py
│   ├── users.py
│   └── jokes.py
├── my_helpers.py
├── my_debug.py
├── main.py
├── company.db
├── Pipfile
├── Pipfile.lock
└── README.md
models/__init__.py - Database connection setup.
models/users.py - User model and database interactions.
models/jokes.py - Joke model and database interactions.
my_helpers.py - Helper functions for CLI operations.
my_debug.py - Debugging utilities and scripts.
main.py - Main script for running the CLI application.
company.db - SQLite database file.
Pipfile - Pipenv file for managing dependencies.
Pipfile.lock - Pipenv lock file for dependencies.
README.md - Project documentation.

#### Contributing
Feel free to submit issues or pull requests for improvements and bug fixes.

#### License
This project is licensed under the MIT License.

#### Acknowledgments
Inspired by the need for a simple joke management system.
Emoji icons from Emojipedia.


