import pymysql



def request(query, verbose=False):
    try:
        db = pymysql.connect(host="localhost",user="root",passwd="abz00ba",db="arunangsukrishna")
    except Exception:
        print("Error in MySQL connexion")
    else:
        cur = db.cursor()
        try:
            cur.execute(query)
        except Exception:
            print("Error with query: " + query)
        else:
            db.commit()
            result = cur.fetchall()
            print(result)
        db.close()


if __name__ =="__main__":
    query = "SELECT VERSION()"
    request(query)


#  http://zetcode.com/python/pymysql/
#  http://book.pythontips.com/en/latest/context_managers.html
