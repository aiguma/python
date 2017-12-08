import pymysql


def dbTest():
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         port=11111,        # your port
                         user="test",  # your username
                         passwd="test!",  # your password
                         db="test")  # name of the data base

    cur = db.cursor()

    cur.execute("SELECT * FROM test_table")

    for row in cur.fetchall():
        print(row[0])

    db.close()


if __name__ == "__main__":
    dbTest()
