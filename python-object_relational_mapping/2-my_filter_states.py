#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
from the hbtn_0e_0_usa database where the name matches the user argument
in ascending order by states.id.
"""

import MySQLdb
import sys


def filter_states_by_name():
    """
    Connects to a MySQL server and prints states matching the given argument
    from the states table sorted by id.
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
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' " \
            "ORDER BY states.id ASC".format(sys.argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_name()
