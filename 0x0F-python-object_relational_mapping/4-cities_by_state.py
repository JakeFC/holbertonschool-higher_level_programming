#!/usr/bin/python3
"""Script which prints each city, along with their id and state in
the given db in argv[3], using argv[1] and [2] for MySQL user and passwd,
respectively.
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM states \
    INNER JOIN cities ON states.id = cities.state_id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close
