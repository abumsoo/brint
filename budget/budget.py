#!/usr/bin/env python

import sqlite3
import readline

# User interface to take in data
## DONE Print out options
## DONE Interactive prompts
### DONE Ask if they want to record spending
### DONE Ask what category
# DONE Method to create a category
# 1/2 method to enter spending
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
                overview(conn)
            elif choice == 'q':
                return False

def mk_table(conn):
    # Create table in database if it doesn't exist
    cur = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS finances
    (Id INTEGER PRIMARY KEY, Date TEXT, Category TEXT, Description TEXT, Amount REAL)"""
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

    # TODO: Figure out expenditure and income (-/+)

    amount = input("Amount: ")
    description = input("Description: ")

    # display existing categories
    unique_query(conn, 'category')
    category = input("Category: ")

    # put into database
    entry(conn, (category, description, float(amount)))

    # TODO: Check against budget for specified category
    budget_check(conn)

def budget_check(conn):
    """ check if user is within budget """
    pass

def unique_query(conn, column):
    """ Print unique values of specified column """

    cur = conn.cursor()
    query = "SELECT DISTINCT {0} FROM finances".format(column)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(' ', row[0])

def entry(conn, col_vals):
    cur = conn.cursor()
    query = "INSERT INTO finances VALUES(NULL, date(), ?, ?, ?)"
    cur.execute(query, col_vals)

    conn.commit()

def capital(conn):
    # set initial capital
    # Insert as a regular entry under capital category 
    query = "INSERT INTO"
    pass

def budget():
    # TODO: Set monthly threshold warning?
    # TODO: Set weekly ""
    # TODO: Set budget for category
    pass

def query(conn, columns):
    cur = conn.cursor()
    query = "SELECT {0}, {1}, {2}, {3} FROM finances".format(*columns)
    cur.execute(query)
    return cur.fetchall()

def overview(conn):
    """ Display overview of finances """

    print()
    print("OVERVIEW")
    print()


    rows = query(conn, ('date','category','description','amount'))

    cat_longest = longest_string_len(conn, 'category')
    desc_longest = longest_string_len(conn, 'description')
    # TODO: Headings
    date_len = longest_string_len(conn, 'date')
    amount_len = longest_string_len(conn, 'amount')
    header = 'Date' + ' ' * (date_len - 2)
    header += 'Category' + ' ' * (cat_longest - 6) + 'Description'
    padding = 80 - len(header) - len('Entry')
    header += ' ' * padding + 'Entry'
    # TODO: If there's no data, formatting is fucked
    print(header)
    print('-' * 80)

    # TODO: if row is bigger than 80, add a newline

    for row in rows:
        date, category, description, amount = row
        amount = "{:.2f}".format(amount)
        # align leftside items between each other
        cat_to_desc = cat_longest - len(category)
        line_out = date + '  ' + category + ' ' * cat_to_desc + '  ' + description
        padding = 80 - (len(amount) + len(line_out))
        line_out += ' ' * padding + amount
        print(line_out)

def header(conn):
    cur = conn.cursor()
    

def longest_string_len(conn, column):
    cur = conn.cursor()
    query = """SELECT {0} FROM finances
    ORDER BY LENGTH({0}) DESC LIMIT 1""".format(column)
    cur.execute(query)
    if not cur.fetchall():
        return 0
    longest_string = cur.fetchall()[0][0]
    return len(str(longest_string))

if __name__ == '__main__':
    main()
