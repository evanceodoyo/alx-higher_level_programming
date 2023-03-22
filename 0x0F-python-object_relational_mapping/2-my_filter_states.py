#!/usr/bin/python3
"""
lists all states matching the argument passed by they user
Parameters given to the script: username, password, and db name, state name.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to the database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         db=argv[3])

    # create cursor (to be use in executing queries)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4],))
    for row in cur.fetchall():
        print(row)

    # close cursor and db
    cur.close()
    db.close()
