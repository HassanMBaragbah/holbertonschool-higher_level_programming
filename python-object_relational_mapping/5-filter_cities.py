#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all cities
of a given state from the hbtn_0e_4_usa database safely against SQL injection.
"""

import MySQLdb
import sys


def filter_cities_by_state():
    """
    Connects to a MySQL server and prints all cities of a specific state
    sorted by cities.id using a single safe execute() call.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities_by_state()
