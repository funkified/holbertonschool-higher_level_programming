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
    cursor.execute("SELECT * FROM states.name\
                    ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for states in rows:
        print("{}".format(states))
    cursor.close()
    conn.close()
