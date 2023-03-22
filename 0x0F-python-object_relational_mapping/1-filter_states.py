#!/usr/bin/python3
"""
lists all values in the table 'states' with name starting with N (upper N)
Parameters given to the script: mysql username, mysql password, and db name.
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'  ORDER BY id ASC")
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)

    # close cursor and db
    cur.close()
    db.close()
