import pymysql

con = pymysql.connect('localhost', 'root',
    'abz00ba', 'arunangsukrishna')

with con:

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    print("Database version: {}".format(version[0]))
