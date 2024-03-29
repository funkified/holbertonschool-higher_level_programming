#!/usr/bin/python3
"""
script that all states from database
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    dbConnect = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3])
    cursor = dbConnect.cursor()
    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name=%s \
    ORDER BY cities.id ASC", (argv[4],))
    print(", ".join(city[0] for city in cursor.fetchall()))
    cursor.close()
    dbConnect.close()
