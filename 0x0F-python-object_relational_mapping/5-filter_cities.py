#!/usr/bin/python3
if __name__ != "__main__":
    exit()
import sys
import MySQLdb
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
state = sys.argv[4];
count = 0;
db = MySQLdb.connect(host="localhost",
                     user=username, passwd=password, db=database_name)
cur = db.cursor()
row_count = cur.execute(
                        ("SELECT states.name, cities.name FROM states INNER JOIN"
                        " cities ON states.id = cities.state_id ORDER BY cities.id"))
for entry in cur.fetchall():
    if entry[0] == state:
        if count == 0:
            print(entry[1], end="")
        else:
            print(",", entry[1], end="")
        count+=1;
if count > 0:
    print("")
