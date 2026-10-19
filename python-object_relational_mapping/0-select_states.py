#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa.
It connects to a MySQL server running on localhost at port 3306.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Connects to MySQL database and prints all states sorted by id.
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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
