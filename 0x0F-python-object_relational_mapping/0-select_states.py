#!/usr/bin/python3

"""
Contains module that lists states in the hbtn_0e_0_usa database
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(localhost, argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id')
