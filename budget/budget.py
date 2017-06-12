#!/usr/bin/env python

import sqlite3
import readline

# User interface to take in data
## Print out options
## Interactive prompts
### Ask if they want to record spending
### Ask what category
# Method to create a category
# method to enter spending
# Method to limit spending in certain categories 'Set budgets'

# Infinite loop until user says quit
def main():
    conn = sqlite3.connect('example.db')
    with conn:
        mk_table(conn)
        while True:
            print_menu()
            choice = input("What would you like to do? ")
            if choice == 'r':
                spent(conn)
            elif choice == 'v':
                print()
                print("Overview")
                overview(conn)
            elif choice == 'q':
                return False

def mk_table(conn):
    # Create table in database if it doesn't exist
    cur = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS finances
    (Id INTEGER PRIMARY KEY, Category TEXT, Description TEXT, Amount REAL)"""
    cur.execute(query)
    conn.commit

def print_menu():
    # TODO: First time user should have an option to input initial capital
    # TODO: Option to clear the database
    # TODO: Option to delete entries
    # TODO: Option to modify entries
    print()
    print("r) Record spending")
    print("v) View spending")
    print("b) Set budget")
    print("q) Quit")
    print()

def spent(conn):
    cur = conn.cursor()
    # TODO: display existing categories
    amount = input("Amount: ")
    description = input("Description: ")
    category = input("Category: ")
    # TODO: Record in database
    query = "INSERT INTO finances VALUES(NULL, ?, ?, ?)"
    cur.execute(query, (category, description, float(amount)))
    conn.commit()
    # TODO: Check against budget for specified category

def budget():
    pass

def overview(conn):
    cur = conn.cursor()
    query = "SELECT amount, description, category FROM finances"
    cur.execute(query)
    rows = cur.fetchall()
    #print("Amount | Description | Category")
    print()
    for row in rows:
        amount = "$" + str(row[0])
        padding = 50-len(row[1])-len(amount)
        print(row[1], ' '*padding, amount)

if __name__ == '__main__':
    main()
