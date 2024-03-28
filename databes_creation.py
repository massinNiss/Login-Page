from mysql import connector

def authenticate_user(username, first_name, last_name, email, password):
    try:
        conn = connector.Connect(host="127.0.0.1", user="root", port="3306", db="identification")
        cursor = conn.cursor()
        print("connection-successfully")

        cursor.execute("SELECT * FROM data WHERE email = %s", (email,))
        result = cursor.fetchone()
        if result== None:
            # insert the user into the database
            sql = ("INSERT INTO data (id, first_name, last_name, email, password, username) VALUES (%s, %s, %s, %s, %s, %s)")
            values = (1, username, first_name, last_name, email, password)
            cursor.execute(sql, values)
            conn.commit()
            return 1
        else:
            return 0
    except connector.Error as e:
        print("++++>>", e)
        return e
