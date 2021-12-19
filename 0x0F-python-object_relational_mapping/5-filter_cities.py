#!/usr/bin/python3
"""
script that all states from database
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])

    cursor = conn.cursor()
    cursor.execute("SELECT cities.name FROM cities\
    JOIN states ON cities.states_id = states.id WHERE states.name=%s\
    ORDER BY cities.id ASC", (argv[4],))

    rows = cursor.fetchall()
    for city in rows:
        city += rows
    print(", ".join(city))

    cursor.close()
    conn.close()
