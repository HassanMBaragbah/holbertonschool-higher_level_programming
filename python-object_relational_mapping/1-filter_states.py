#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
with a name starting with 'N' from the hbtn_0e_0_usa database
in ascending order by id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
