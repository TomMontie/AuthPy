from flask import Flask, render_template, request, redirect, url_for, flash
from auth import sign_up, login
from models import setup_database



def main():
    setup_database()

    print("Welcome to the Authentication System!")
    while True:
        choice = input("Do you want to [1] Sign Up or [2] Login? (Enter 'q' to quit): ")

        if choice == '1':
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            sign_up(username, password)
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login(username, password)
        elif choice.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()