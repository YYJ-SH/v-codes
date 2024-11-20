import sqlite3

def secure_function(user_input):
    query = "SELECT * FROM users WHERE username = ?"

    try:
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()

        print(f"Executing query: {query} with input: {user_input}")
        cursor.execute(query, (user_input,))  # 사용자 입력을 안전하게 바인딩

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

# 사용자 입력값
user_input = "'; DROP TABLE users; --"
secure_function(user_input)
