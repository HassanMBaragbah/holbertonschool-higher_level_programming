#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all cities
along with their corresponding states from the hbtn_0e_4_usa database
in ascending order by cities.id using a single execute() call.
"""

import MySQLdb
import sys


def list_cities_by_state():
    """
    Connects to a MySQL server and prints all cities with their states
    from the cities and states tables sorted by cities.id.
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
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_state()
