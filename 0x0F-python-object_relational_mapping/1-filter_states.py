#!/usr/bin/python3
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
for entry in cur.fetchall():
    if entry[1][0] == "N":
        print(entry)
