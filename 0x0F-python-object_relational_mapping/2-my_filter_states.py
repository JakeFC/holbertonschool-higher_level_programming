#!/usr/bin/python3
"""Script which prints each state whose name matches argv[4] with its id from
the given db in argv[3], using argv[1] and [2] for MySQL user and passwd,
respectively
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states")
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    db.close
