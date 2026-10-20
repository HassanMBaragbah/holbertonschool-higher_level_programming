#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
from the hbtn_0e_0_usa database in ascending order by states.id.
"""

import MySQLdb
import sys


def select_states():
    """
    Connects to the database and prints all the states sorted by id.
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
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    select_states()
