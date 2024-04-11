#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
"""
if __name__ != "__main__":
    exit()
import sys
import MySQLdb
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
db = MySQLdb.connect(host="localhost",
                     user=username, passwd=password, db=database_name)
cur = db.cursor()
row_count = cur.execute("SELECT * FROM states ORDER BY id")
for i in range(0, row_count):
    row = cur.fetchone()
    print(row)
