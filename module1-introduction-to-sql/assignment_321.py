import sqlite3

def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


# Assignment Queries Begin Here -
# 1. Total # of Characters
char_count = """
SELECT COUNT(character_id)
FROM charactercreator_character;
"""

# 2. How many in each character sub-class
# Will have to write a new one for each class
# Sum total and compare to #1
fighter_count = \
    """ SELECT COUNT (character_ptr_id) FROM charactercreator_fighter;"""

cleric_count = \
    """SELECT COUNT (character_ptr_id) FROM charactercreator_cleric;"""

thief_count = \
    """SELECT COUNT (character_ptr_id) FROM charactercreator_thief;"""

mage_count = \
    """SELECT COUNT (character_ptr_id) FROM charactercreator_mage;"""

necro_count = \
    """SELECT COUNT (mage_ptr_id) FROM charactercreator_necromancer;"""

# 3. Total # of items
total_items = \
    """SELECT COUNT(item_id) FROM armory_item;"""

# 4. How many items are weapons? How many are not?
# """SELECT COUNT (item_ptr_id) FROM armory_weapon""" - possible
total_weap = \
    """ SELECT COUNT(DISTINCT item_id) FROM armory_item, armory_weapon 
    WHERE item_id = item_ptr_id;"""

# 5. How many items does each character have? - Return first 20
item_count_per_char = """
SELECT COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""

# COME BACK TO THIS - HOW DID I GET 137 AGAIN?
# DB_Browser - all items above 137 are weapons

# 6. How many weapons does each character have? - Return first 20
weap_count_per_char = """
SELECT COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id > 137
GROUP BY character_id
LIMIT 20;
"""

# 7. On average, how many items does each character have?
item_count_avg = """
SELECT AVG(items.avg_count) FROM
(SELECT COUNT(item_id) AS avg_count
FROM charactercreator_character_inventory
GROUP BY character_id) AS items;
"""

# 8. On average, how many weapons does each character have?
weap_count_avg = """
SELECT AVG(weapons.avg_count) FROM
(SELECT COUNT(item_id) AS avg_count
FROM charactercreator_character_inventory
WHERE item_id > 137
GROUP BY character_id) AS weapons;
"""


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()

    # The query is the SQL code written above - I only called this variable
    # query because we execute the query here
    query1 = execute_query(curs, char_count)[0][0]
    print('1. How many total characters are there?')
    print(f'There are a total of {query1} characters currently existing\n')

    query2_fighter = execute_query(curs, fighter_count)[0][0]
    query2_cleric = execute_query(curs, cleric_count)[0][0]
    query2_thief = execute_query(curs, thief_count)[0][0]
    query2_mage = execute_query(curs, mage_count)[0][0]
    query2_necro = execute_query(curs, necro_count)[0][0]
    print('2. How many are there in every subclass?')
    print(f'There are {query2_fighter} fighters, {query2_thief} thieves, '
          f'{query2_cleric} clerics(priests), {query2_mage - query2_necro} '
          # because necromancer is a subclass of mage
          f'mages and {query2_necro} necromancers\n')

    query3 = execute_query(curs, total_items)[0][0]
    print('3. How many items are in the game?')
    print(f'There are {query3} total items that have been generated\n')

    query4 = execute_query(curs, total_weap)[0][0]
    print('4. Of these items, how many are weapons? How many are not?')
    print(f'There are {query4} weapons and {query3 - query4} '
          f'items that are not weapons\n')

    query5 = execute_query(curs, item_count_per_char)[0: 20]
    print('5. How many items are the characters holding?')
    print(f'Here are the 20 characters and how many items they are holding:\n'
          f'{query5}\n')

    query6 = execute_query(curs, weap_count_per_char)[0: 20]
    print('6. How many weapons are the characters holding?')
    print(f'Here are the 20 characters and the # of weapons they have:\n'
          f'{query6}\n')

    query7 = execute_query(curs, item_count_avg)[0][0]
    print('7. What is the average number of items held?')
    print(f'The average number of items held is {query7}\n')

    query8 = execute_query(curs, weap_count_avg)[0][0]
    print('8. What is the average number of weapons held? ')
    print(f'The average number of weapons held is {query8}\n')
