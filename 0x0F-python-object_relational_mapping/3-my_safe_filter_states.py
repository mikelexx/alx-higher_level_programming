#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states\
table of hbtn_0e_0_usa where name matches the argument.\
But this time, write one that is safe from MySQL injections!
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    match_string = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=password, db=database_name)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE
                   name LIKE BINARY %s ORDER BY id""", (match_string,))
    for entry in cur.fetchall():
        print(entry)
