#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connect = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute(
            "SELECT cities.id, cities.name, states.name FROM cities \
                    INNER JOIN states ON states.id=cities.state_id")
    rows_selected = db_cursor.fetchall()
    for row in rows_selected:
        print(row)
    db_cursor.close()
    db_connect.close()
