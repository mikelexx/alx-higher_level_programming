#!/usr/bin/python3
"""
Write a script that lists all states with a name starting \
with N (upper N) from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=password, db=database_name)
    cur = db.cursor()
    row_count = cur.execute("SELECT * FROM states ORDER BY id")
    for entry in cur.fetchall():
        if entry[1][0] == "N":
            print(entry)
