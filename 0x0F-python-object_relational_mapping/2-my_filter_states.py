#!/usr/bin/python3
"""
Write a script that takes in an argument and displays\
all values in the states table of hbtn_0e_0_usa where\
name matches the argument.
"""
import sys
import MySQLdb
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    match_string = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=password, db=database_name)
    cur = db.cursor()
    table = cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id"
                        .format(match_string.strip("'")))
    for row in cur.fetchall():
        print(row)
