#!/usr/bin/python3
"""Script which prints each city from the state given in argv[4] in
the given db in argv[3], using argv[1] and [2] for MySQL user and passwd,
respectively.
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON \
    cities.state_id = states.id WHERE BINARY states.name = %s", (argv[4],))
    rows = cursor.fetchall()
    l = []
    for row in rows:
        l.append(row[0])
    print(", ".join(l))
    db.close
