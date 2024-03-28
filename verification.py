from mysql import connector

def verify(usr, pswd):
    conn = connector.Connect(host="127.0.0.1", user="root", port="3306", db="identification")
    cur = conn.cursor()
    cur.execute("select * from data where username=%s and password =%s ", (usr, pswd))
    row = cur.fetchone()
    if row == None:
        return 0
    else:
        return 1