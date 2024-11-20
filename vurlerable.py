import sqlite3

def vulnerable_function(user_input):
    # SQL Injection 취약점: 사용자 입력값을 그대로 쿼리에 삽입
    query = f"SELECT * FROM users WHERE username = '{user_input}'"

    try:
        # SQLite 데이터베이스 연결 (로컬 파일 데이터베이스 사용)
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()

        print(f"Executing query: {query}")
        cursor.execute(query)

        # 결과 출력
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # 데이터베이스 연결 닫기
        if conn:
            conn.close()

# 사용자 입력값 (SQL Injection 테스트)
user_input = "'; DROP TABLE users; --"  # SQL Injection Payload
vulnerable_function(user_input)
