#!/usr/bin/python3
import sys
import MySQLdb

"""
script that lists all states from database hbtn_0e_0_usa
Usage: mysql username, mysql password and database name
"""
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute(
            "SELECT * FROM states WHERE Name LIKE BINARY 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    ur.close()
    conn.close()
