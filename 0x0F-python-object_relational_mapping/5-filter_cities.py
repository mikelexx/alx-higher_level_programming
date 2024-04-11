#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and\
lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    count = 0
    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=password, db=database_name)
    cur = db.cursor()
    row_count = cur.execute("""SELECT states.name,
                             cities.name FROM states INNER JOIN
                             cities ON states.id = cities.state_id
                            WHERE states.name LIKE BINARY %s ORDER BY
                             cities.id""", (state_name,))
    for entry in cur.fetchall():
        if count == 0:
            print(entry[1], end="")
        else:
            print(",", entry[1], end="")
        count += 1
    print("")
