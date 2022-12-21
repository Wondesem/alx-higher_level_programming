#!/usr/bin/python3
import sys
import MySQLdb

"""
script that lists all states from database hbtn_0e_0_usa
Usage: mysql username, mysql password and database name
"""
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
