#!/usr/bin/python3
"""
Write a script that takes in an argument and displays\
all values in the states table of hbtn_0e_0_usa where\
name matches the argument.
"""
if __name__ != "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    match_string = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=password, db=database_name)
    cur = db.cursor()
    table = cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                        (match_string,))
    for row in cur.fetchall():
        print(row)
