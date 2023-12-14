#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connect = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute(
            "SELECT cities.name FROM cities INNER JOIN states \
                    ON states.id=cities.state_id WHERE states.name \
                    LIKE BINARY %(state_name)s", {'state_name': argv[4]})
    rows_selected = db_cursor.fetchall()
    if rows_selected is not None:
        print(", ".join([row[0] for row in rows_selected]))
    db_cursor.close()
    db_connect.close()
