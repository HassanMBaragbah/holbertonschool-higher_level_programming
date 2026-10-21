#!/usr/bin/python3
"""
This module connects to a MySQL database and safely lists all states
from the hbtn_0e_0_usa database where the name matches the user argument
while preventing SQL injection vulnerabilities.
"""

import MySQLdb
import sys


def safe_filter_states():
    """
    Connects to a MySQL server and safely
    prints states matching the given argument
    from the states table sorted by id using parameterized queries.
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
