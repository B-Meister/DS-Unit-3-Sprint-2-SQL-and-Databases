import sqlite3
import pandas as pd

connect = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = connect.cursor()
# makes the database with sqlite3

df1 = pd.read_csv('buddymove_holidayiq.csv')
# read csv

drop_buddy = """
DROP TABLE buddy
"""
curs.execute(drop_buddy)
# dropping the buddy table so it can be run again

df1.to_sql('buddy', connect)
# convert csv file into an sql database

if __name__ == '__main__':
    # 1. Count how many rows you have
    curs.execute('SELECT COUNT (*) FROM buddy')
    print(f'There are a total of {curs.fetchall()[0][0]} rows in the database')

    # 2. How many users reviewed atleast 100 Nature + reviewed atleast 100 Shopping
    curs.execute('SELECT COUNT (*) FROM buddy WHERE Nature > 99 AND Shopping > 99')
    print(f'There are {curs.fetchall()[0][0]} people who reviewed at least 100 '
          f'Nature AND Shopping locations')

    # 3. What are the average number of review for each category?
    # curs.execute('SELECT AVG COUNT (*) FROM buddy')
    # print(f'{curs.fetchall()}')
