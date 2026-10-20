#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
from the hbtn_0e_0_usa database in ascending order by id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to the database using command-line arguments
    and prints all states from the states table.
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
