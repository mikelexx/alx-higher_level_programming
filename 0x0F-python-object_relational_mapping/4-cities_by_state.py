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
row_count = cur.execute(
        ("SELECT cities.id, cities.name, states.name"
            " FROM cities LEFT JOIN"
            " states ON cities.state_id=states.id"
            " ORDER BY cities.id"))
for entry in cur.fetchall():
    print(entry)
