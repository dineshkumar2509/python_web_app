import psycopg2


def doDBUpdate(query, args):
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='db' password='my_app_pass'")
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    cur.close()
    conn.close()


def doSelectFirst(query, args=None):
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='db' password='my_app_pass'")
    cur = conn.cursor()
    if args:
        cur.execute(query, args)
    else:
        cur.execute(query)
    res = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return res


def doSelectList(query):
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='db' password='my_app_pass'")
    cur = conn.cursor()
    cur.execute(query)
    res = []
    for row_item in cur:
        res.append(row_item[0])
    conn.commit()
    cur.close()
    conn.close()
    return res

