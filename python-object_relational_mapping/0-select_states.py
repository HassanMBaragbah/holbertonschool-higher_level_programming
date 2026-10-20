#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
from the hbtn_0e_0_usa database in ascending order by states.id.
"""

import MySQLdb
import sys


"""
Connects to a MySQL server and prints all states
from the states table sorted by id.
"""
if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
